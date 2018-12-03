## md5加密
>import hashlib

pwd = '123123'
m = hashlib.md5()
m.update(pwd.encode("utf-8"))#参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
print(m.hexdigest())