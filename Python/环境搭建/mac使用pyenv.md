## mac使用pyenv

安装pyenv
    brew update

    brew install zlib

    brew install pyenv

    brew install pyenv-virtualenv
    
修改 bash_profile 自动启动

    vim ~/.bash_profile
    
    //eval "$(pyenv init -)"
    //eval "$(pyenv virtualenv-init -)"
    
    if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
    if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

安装python并创建虚拟环境

    pyenv init

    CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install -v 3.5.5

    pyenv virtualenv 3.5.5 py35
    
    pyenv rehash