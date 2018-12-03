# Django-rest-framework-JWT
### time : 2017.7.30
## content
## 安装要求：

 - Python（2.7,3.3,3.4,3.5）
 - Django（1.8，1.9，1.10）
 - Django REST框架（3.0,3.1,3.2,3.3,3.4,3.5）
 - 可选 Pycharm(...)
 - 如果是 Windows 系统 建议装一个接口测试器 postman 之类的
 
## 安装方法
1. 可以使用 pip  
    $ pip install djangorestframework-jwt
2. 使用 Pycharm  
   File -> settings -> Project:项目名 -> Project Interpreter -> 点“ + ”号  ->  搜索 djangrestframework 即可
## 用法
在你的 settings.py，添加 JSONWebTokenAuthentication 到 Django REST 框架 DEFAULT\_AUTHENTICATION\_CLASSES。

	REST_FRAMEWORK = {
	    'DEFAULT_PERMISSION_CLASSES': (
	        'rest_framework.permissions.IsAuthenticated',
	    ),
	    'DEFAULT_AUTHENTICATION_CLASSES': (
	        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
	        'rest_framework.authentication.SessionAuthentication',
	        'rest_framework.authentication.BasicAuthentication',
	    ),
	}

在 urls.py 添加以下 URL 路由以通过 POST 获取令牌包括用户的用户名和密码。

	from rest_framework_jwt.views import obtain_jwt_token
	#...
	
	urlpatterns = [
	    '',
	    # ...
	
	    url(r'^api-token-auth/', obtain_jwt_token),
	]
如果 用户名为 admin 和 password password123 创建了用户，可以通过在终端中执行以下操作来轻松测试端点是否正常工作。
	
	$ curl -X POST -d "username=admin&password=password123" http://localhost:8000/api-token-auth/
或者，您可以使用 Django REST 框架支持的所有内容类型来获取验证令牌。例如：

	
现在为了访问受保护的 api urls，你必须包含 Authorization: JWT <\your_token> 头。

	$ curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/
##刷新令牌
如果 JWT\_ALLOW\_REFRESH 是真，则不过期的令牌可以“刷新”以获得具有更新的到期时间的全新令牌。添加如下URL格式：

    from rest_framework_jwt.views import refresh_jwt_token
    #  ...

    urlpatterns = [
        #  ...
        url(r'^api-token-refresh/', refresh_jwt_token),
    ]
将现有令牌传递到刷新端点，如下所示： **{"token": EXISTING\_TOKEN}**。  
请注意，只有未过期的令牌才能正常工作。JSON响应看起来与正常获取令牌端点相同  **{"token": NEW_TOKEN}**。

	$ curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8000/api-token-refresh/
可以重复使用令牌进行刷新（token1 - > token2 - > token3），但是该令牌链存储原始令牌（用用户名/密码凭据获取）的时间，as orig\_iat。您只能保持清醒令牌  JWT\_REFRESH\_EXPIRATION\_DELTA。

一个典型的用例可能是一个网络应用程序，您希望让用户“登录”该网站，而无需重新输入密码，或者在令牌过期之前被惊讶地踢出来。想象一下，他们有一个1小时的令牌，只是在最后一分钟，而他们还在做某事。使用移动设备，您可以存储用户名/密码以获取新的令牌，但这在浏览器中不是一个好主意。每次用户加载页面时，都可以检查是否存在未过期的令牌，如果它接近到期，则刷新它以扩展其会话。换句话说，如果用户正在积极使用您的网站，他们可以保持他们的“会话”活着。  
因为 orig\_iat 领域默认是 False 所以需要提前设置

	JWT_AUTH = {
        'JWT_ALLOW_REFRESH': True,
	}

否则会报异常

	{
	    "non_field_errors": [
	        "orig_iat field is required."
	    ]
	}


##验证令牌
在一些微服务架构中，身份验证由单一服务来处理。其他服务委托确认用户登录到此认证服务的责任。这通常意味着服务将通过从用户接收到的认证服务的JWT，并等待确认JWT在将受保护的资源返回给用户之前是有效的。

此程序包使用验证端点支持此设置。添加以下URL模式：

    from rest_framework_jwt.views import verify_jwt_token

    #...

    urlpatterns = [
        #  ...
        url(r'^api-token-verify/', verify_jwt_token),
    ]
将令牌传递给验证端点将返回200个响应，如果令牌有效则返回该令牌。否则，它将返回一个400错误请求以及一个错误，识别令牌无效的原因。

	$ curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8000/api-token-verify/
##附加设置
还有一些额外的设置，您可以重写类似于 Django REST 框架本身。以下是所有可用的默认值。

	JWT_AUTH = {
	    'JWT_ENCODE_HANDLER':
	    'rest_framework_jwt.utils.jwt_encode_handler',
	
	    'JWT_DECODE_HANDLER':
	    'rest_framework_jwt.utils.jwt_decode_handler',
	
	    'JWT_PAYLOAD_HANDLER':
	    'rest_framework_jwt.utils.jwt_payload_handler',
	
	    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
	    			  		'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
	
	    'JWT_RESPONSE_PAYLOAD_HANDLER':
	    'rest_framework_jwt.utils.jwt_response_payload_handler',
	
	    'JWT_SECRET_KEY': settings.SECRET_KEY,
	    'JWT_GET_USER_SECRET_KEY': None,
	    'JWT_PUBLIC_KEY': None,
	    'JWT_PRIVATE_KEY': None,
	    'JWT_ALGORITHM': 'HS256',
	    'JWT_VERIFY': True,
	    'JWT_VERIFY_EXPIRATION': True,
	    'JWT_LEEWAY': 0,
	    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
	    'JWT_AUDIENCE': None,
	    'JWT_ISSUER': None,
	
	    'JWT_ALLOW_REFRESH': False,
	    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
	
	    'JWT_AUTH_HEADER_PREFIX': 'JWT',
	    'JWT_AUTH_COOKIE': None,
	
	}
此软件包使用 JSON Web Token Python 实现，PyJWT，并允许修改其中的一些可用选项。

- JWT\_SECRET\_KEY  
这是用于签署JWT的秘密密钥。确保这是安全的，不是共享的或公开的。  
默认是你的项目 settings.SECRET\_KEY。

- JWT\_GET\_USER\_SECRET\_KEY  
这是更强大的 JWT\_SECRET\_KEY 版本。它是根据用户定义的，因此，在令牌受到威胁的情况下，所有者可以轻松地更改它。更改此值将使给定用户的所有令牌不可用。值应该是一个函数，接受用户作为参数并返回它的秘密密钥。    
  默认是None。

- JWT\_PUBLIC\_KEY  
这是一个类型的对象 cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey 。它将用于验证传入的JWT的签名。 JWT\_SECRET\_KEY 设置时将覆盖。阅读文档了解更多详情。请注意，JWT\_ALGORITHM 必须设置为一个 RS256，RS384或RS512。  
默认是None。

- JWT\_PRIVATE\_KEY  
这是一个类型的对象cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey。它将用于签署JWT的签名组件。 JWT\_SECRET_KEY 设置时将覆盖。阅读文档了解更多详情。请注意，JWT\_ALGORITHM 必须设置为一个 RS256，RS384或RS512。  
默认是None。

- JWT\_ALGORITHM  
可能的值是 PyJWT 中加密签名的任何支持的算法。  
默认是"HS256"。

- JWT\_VERIFY  
如果这个秘密是错误的，那么会引发一个 jwt.DecodeError 告诉你。你仍然可以通过设置到 JWT\_VERIFY 达到有效负载False。  
默认是True。

- JWT\_VERIFY\_EXPIRATION  
您可以通过设置关闭到期时间的验证JWT\_VERIFY\_EXPIRATION来False。没有到期验证，JWT 将永远持续，意味着一个泄漏的令牌可以无限期地被攻击者使用。  
默认是True。

- JWT\_LEEWAY  
这允许您验证过去但不是很远的到期时间。例如，如果您的JWT有效载荷在创建后设置为30秒，但您知道有时您将在30秒后处理它，您可以设置10秒的余地以获得一定的余量。  
默认值为0秒。

- JWT\_EXPIRATION\_DELTA  
这是 Python 的一个实例 datetime.timedelta。这将被添加到          datetime.utcnow() 设置到期时间。  
默认为 datetime.timedelta(seconds=300)（5分钟）。
 
- JWT\_AUDIENCE  
这是一个字符串，将根据aud令牌的字段进行检查（如果存在）。  
默认值为None（如果aud存在于JWT 则失败）。

- JWT\_ISSUER  
这是一个字符串，它将根据 iss 令牌的字段进行检查。  
默认是 None（不要检查issJWT）。

- JWT\_ALLOW\_REFRESH  
启用令牌刷新功能。令牌  rest_framework\_jwt.views.obtain\_jwt\_token 将会有一个 orig\_iat 领域。  
默认是 False

- JWT\_REFRESH\_EXPIRATION\_DELTA  
限制令牌刷新，是一个 datetime.timedelta 实例。这是原始令牌之后的时间，未来的令牌可以被刷新。 
默认为 datetime.timedelta(days=7)（7天）。

- JWT\_PAYLOAD\_HANDLER  
指定一个自定义函数来生成令牌有效负载

- JWT\_PAYLOAD\_GET\_USER\_ID\_HANDLER  
如果 user_id 与默认有效负载处理程序的存储方式不同，请执行此功能 user_id 从有效负载中提取。注意：将不赞成JWT\_PAYLOAD\_GET\_USERNAME\_HANDLER。

- JWT\_PAYLOAD\_GET\_USERNAME\_HANDLER  
如果 username 与默认有效负载处理程序的存储方式不同，请执行此功能 username 从有效负载中提取。

- JWT\_RESPONSE\_PAYLOAD\_HANDLER  
负责控制登录或刷新后返回的响应数据。覆盖以返回自定义响应，例如包括用户的序列化表示。  
默认返回JWT令牌。 
		例：
		
		def jwt_response_payload_handler(token, user=None, 	request=None):
			return {
				'token': token,
				'user': UserSerializer(user, context={'request': request}).data
		}
		默认是 {'token': token}

- JWT\_AUTH\_HEADER\_PREFIX  
您可以修改与令牌一起发送的必需的授权头值前缀。默认值为 JWT 。这个决定是在 PR ＃4 中引入的，允许在 DRF 中使用这个包和 OAuth2。  
用于令牌和授权标头的另一个常用值是 Bearer。  
默认是 JWT。

- JWT\_AUTH\_COOKIE  
如果要使用 http Cookie，除了授权标头作为令牌的有效传输之外，可以将其设置为字符串。您在此处设置的字符串将用作请求令牌时将在响应标头中设置的 cookie 名称。令牌验证过程也将调查此 cookie，如果设置。如果请求中存在头和 cookie，则“授权”标题优先。  
默认是 None，在创建令牌时不设置 cookie，也不会在验证时被接受。

##扩展 JSONWebTokenAuthentication
现在 JSONWebTokenAuthentication 假设 JWT 将进入标题，或者配置为 cookie（参见 JWT\_AUTH\_COOKIE ）。JWT规范不要求（请参阅： Making a service Cal ）。例如，JWT可能会进入查询字符串。在用户无法设置头（例如HTML中的src元素）的情况下，需要在查询字符串中发送JWT的能力。

为了实现这一功能，用户可以编写一个自定义Authentication：

	class JSONWebTokenAuthenticationQS(BaseJSONWebTokenAuthentication):
	    def get_jwt_value(self, request):
	         return request.QUERY_PARAMS.get('jwt')
建议使用 BaseJSONWebTokenAuthentication 新的基类，解析HTTP标头时不会有逻辑。

##手动创建新令牌
有时您可能需要手动生成令牌，例如，在创建帐户后立即将令牌返回给用户。你可以这样做：
	
	from rest_framework_jwt.settings import api_settings
	
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	
	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)
**使用postman测试类似**