##Django自定义User模型和登录验证
用户表已存在（与其他App共用），不能再使用Django内置的User模型和默认的登录认证。但是还想使用Django的认证框架（真的很方便啊）。

两个步骤：
1）自定义Use模型，为了区分系统的User模型，命名为Account。
>class Account(models.Model):
    business_email = models.EmailField()
    business_password = models.CharField(max_length=20)
    contact_first_name = models.CharField(max_length=30)
    contact_last_name = models.CharField(max_length=30)
    is_active = models.BooleanField()

    def is_authenticated(self):
        return True

    def hashed_password(self, password=None):
        if not password:
            return self.business_password
        else:
            return hashlib.md5(password).hexdigest()

    def check_password(self, password):
        if self.hashed_password(password) == self.business_password:
            return True
        return False

    class Meta:
        db_table = "bussinesses"


2）自定义登录验证后台，并加入AUTHENTICATION_BACKENDS。
# auth.py

from coocaca.myauth.models import Account

class MyCustomBackend:

    def authenticate(self, business_email=None, business_password=None):
        try:
            user = Account.objects.get(business_email=business_email)
        except Account.DoesNotExist:
            pass
        else:
            if user.check_password(business_password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None


在settings.py中加入该验证后台：
>AUTHENTICATION_BACKENDS = (

    'coocaca.myauth.auth.MyCustomBackend',

)


这样Django就会使用MyCustomBackend作为登录验证后台。

验证通过后返回的是我们自定义的Account模型，并且request.user中获取的也是我们的Account模型（这正是MyCustomBackend中get_user方法的功能）。