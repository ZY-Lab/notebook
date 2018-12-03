##django-redis 配置
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",  # cache backend
                # "PASSWORD": "mysecret",
                "PICKLE_VERSION": -1,  # Use the latest protocol version
                # 套接字超时
                "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
                "SOCKET_TIMEOUT": 5,  # in seconds
                # 压缩支持激活
                # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
                # "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",  # lzma 压缩
                # 忽略连接异常
                # "IGNORE_EXCEPTIONS": True,
                # 配置默认连接池
                "CONNECTION_POOL_KWARGS": {"max_connections": 100},
                # 可扩展解析器
                # "PARSER_CLASS": "redis.connection.HiredisParser",
                # 可扩展序列器   json 序列化数据
                # "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
            },
            "KEY_PREFIX": "example"
        }
    }
 # session backend
>SESSION_ENGINE = "django.contrib.sessions.backends.cache" 
>SESSION_CACHE_ALIAS = "default"
# 日志忽略异常
> DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True  

## Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15


##启动项目前请先启动 redis缓存型数据库下载网址
##https://pan.baidu.com/s/1jItfrRg   密码;bofh (windows版)
###双击redis-server.exe 即可启动     窗口不可关闭

###压缩，解析器，序列器扩展要下载对应文件

##使用
####方法一
> ####from django.core.cache import cache
> ####cache.set( key , value , 有效时间)
> ####cache.get(key);
####方法二(装饰器)
>from django.views.decorators.cache import cache_page, never_cache

>from django.conf import settings

>from django.core.cache.backends.base import DEFAULT_TIMEOUT

>CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

>@cache_page(CACHE_TTL)

注意这是根据URL进行缓存，会缓存整个页面谨慎测试操作