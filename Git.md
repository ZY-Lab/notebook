# Git使用

#### 报错
fatal: The remote end hung up unexpectedly
error: RPC failed; curl 18 transfer closed with outstanding read data remaining
#### 解决
> git config --global http.postBuffer 524288000
> git config --list
