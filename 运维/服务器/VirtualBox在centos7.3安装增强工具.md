## VirtualBox在centos7.3安装增强工具

挂载虚拟光盘
>sudo mount /dev/cdrom /media

安装内核和gcc组件
>yum install -y bzip2 kernel-devel gcc

重新启动机器

进行安装
>cd /media/

>sh VBoxLinuxAdditions.run

控制界面取消自动挂载
挂载命令
>mount -t vboxsf share /mnt/share

取消挂载命令
>umount /mnt/share