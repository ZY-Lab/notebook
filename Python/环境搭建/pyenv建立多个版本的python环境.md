pyenv可以帮助你在一台开发机上建立多个版本的python环境， 并提供方便的切换方法。
virtualenv可以搭建虚拟且独立的python环境，可以使每个项目环境与其他项目独立开来，保持环境的干净，解决包冲突问题。
首先我们可以用pyenv 安装多个python 版本， 比如安装了2.5, 2.6, 3.3 三个版本。 用户可以随意切换当前默认的python版本。 但这时候， 每个版本的环境仍是唯一的， 如果我们想在环境中安装一些库的话， 还是会导致这个版本的环境被修改。 这个时候， 如果我们用virtual env去建立虚拟环境， 就可以完全保证系统路径的干净。无论你在虚拟环境中安装了什么程序， 都不会影响已安装版本的系统环境。 

1.ubuntu安装
>apt install libssl-dev git
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec $SHELL -l
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv  
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile

2.centos安装
yum install git -y
yum install readline readline-devel readline-static -y
yum install openssl openssl-devel openssl-static -y
yum install sqlite-devel -y
yum install bzip2-devel bzip2-libs -y
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec $SHELL -l
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv  
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile

2.常用命令
直接输入pyenv可以列出常用的命令
>pyenv

部分结果如下
>Some useful pyenv commands are:
commands    List all available pyenv commands
local    Set or show the local application-specific Python version

查看可安装的版本
>pyenv install --list

部分结果如下
>Available versions:
2.1.3
2.2.3
2.3.7

查看已安装的版本
>pyenv versions

结果如下
>system (set by /home/wpp/.pyenv/version)

其中的*表示当前使用的版本,system表示当前系统的版本
安装python 3.5.1
>pyenv install 3.5.1

这时执行pyenv versions结果如下
>system (set by /home/wpp/.pyenv/version)
3.5.1

切换默认版本为 3.5.1
>pyenv global 3.5.1

再次执行
>pyenv versions

结果如下
>system (set by /home/wpp/.pyenv/version)
3.5.1
 
想要切回系统默认版本,执行  pyenv global system  即可
要卸载某个版本的python执行
>pyenv uninstall x.x.x
 
3.虚拟环境设置
用以上方式安装会集成virtualenv,所以我们就不用额外安装了
创建虚拟环境
>pyenv virtualenv 3.5.1 py3env
    
这样会创建一个名为py3env的虚拟环境,位于~/.pyenv/versions/目录,其中的3.5.1为python版本号,可以视情况换为你需要的版本
此时执行pyenv versions结果如下
>system (set by /home/wpp/.pyenv/version)
3.5.1
3.5.1/envs/py3env
py3env

其中的py3env是一个链接文件,位于~/.pyenv/versions/,指向~/.pyenv/versions/3.5.1/envs/py3env
进入虚拟环境
>pyenv activate py3env

此时命令行前面会有提示,如下所示
>(py3env) wpp@linuxmint ~ $

注意前面的(py3env)提示符
退出虚拟环境
>pyenv deactivate

在虚拟环境进行的所有操作都针对当前环境,不会污染系统,也不会版本错乱
要删除虚拟环境只需执行
>rm -rf ~/.pyenv/versions/py3env/
rm -rf ~/.pyenv/versions/3.5.1/envs/py3env

如果觉得进入和退出python虚拟环境麻烦,可以在~/.bashrc中加入
>alias py3env="pyenv activate py3env"
alias py3env_exit="pyenv deactivate"

这样进入和退出虚拟环境只需执行
>py3env和py3env_exit