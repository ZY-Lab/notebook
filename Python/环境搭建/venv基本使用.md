# venv基本使用

创建一个文件夹，使用venv模块创建一个名为test的虚拟环境。 

    D:\>mkdir test_venv
    D:\>cd test_venv
    D:\test_venv>python -m venv test
     
启动虚拟环境  

    D:\test_venv>test\Scripts\activate.bat
    (test) D:\test_venv>
    使用'python -m pip install --upgrade pip'命令更新pip
    
退出虚拟环境

    (test) D:\test_venv>test\Scripts\deactivate.bat
    D:\test_venv>