## Django基本指令
### 获取翻译字段
> django-admin makemessages -l zh_Hans
### 编译翻译文件
> django-admin compilemessages
### 验证模型的有效性
> python manage.py validate
### 制作模型迁移文档
> python manage.py makemigrations
### 压缩迁移文档
> python manage.py squashmigrations myapp 0004
### 模型迁移
> python manage.py migrate
### 收集静态文件
> python manage.py collectstatic
### 创建管理员用户
> python manage.py createsuperuser