#Git##
---
  同生活中的许多伟大事物一样，Git 诞生于一个极富纷争大举创新的年代。

　　Linux 内核开源项目有着为数众广的参与者。 绝大多数的 Linux 内核维护工作都花在了提交补丁和保存归档的繁琐事务上（1991－2002年间）。 到 2002 年，整个项目组开始启用一个专有的分布式版本控制系统 BitKeeper 来管理和维护代码。

　　到了 2005 年，开发 BitKeeper 的商业公司同 Linux 内核开源社区的合作关系结束，他们收回了Linux 内核社区免费使用 BitKeeper 的权力。 这就迫使 Linux 开源社区（特别是 Linux 的缔造者Linux Torvalds）基于使用 BitKcheper 时的经验教训，开发出自己的版本系统。 他们对新的系统制订了若干目标：

-	速度
-	简单的设计
-	对非线性开发模式的强力支持（允许成千上万个并行开发的分支）
-	完全分布式

有能力高效管理类似 Linux 内核一样的超大规模项目（速度和数据量）

　　自诞生于 2005 年以来，Git 日臻成熟完善，在高度易用的同时，仍然保留着初期设定的目标。 它的速度飞快，极其适合管理大项目，有着令人难以置信的非线性分支管理系统。

　　Git迅速成为最流行的分布式版本控制系统，尤其是2008年，GitHub网站上线了，它为开源项目免费提供Git存储，无数开源项目开始迁移至GitHub，包括jQuery，PHP，Ruby等等。

#Git是什么
---
Git是一款免费、开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。

　　Git是一个开源的分布式版本控制系统，用以有效、高速的处理从很小到非常大的项目版本管理。Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。

##Git特点##
分布式相比于集中式的最大区别在于开发者可以提交到本地，每个开发者通过克隆（git clone），在本地机器上拷贝一个完整的Git仓库。

-	**直接记录快照，而非差异比较** ： Git 更像是把变化的文件作快照后，记录在一个微型的文件系统中。
-	**近乎所有操作都是本地执行 **：在 Git 中的绝大多数操作都只需要访问本地文件和资源，不用连网。
-	**时刻保持数据完整性** ：在保存到 Git 之前，所有数据都要进行内容的校验和（checksum）计算，并将此结果作为数据的唯一标识和索引。
-	**多数操作仅添加数据** ：常用的 Git 操作大多仅仅是把数据添加到数据库。  

　　开发流程示意图：

![liucheng](https://segmentfault.com/img/bVpR5n)

---
#集中版本控制#
CVS及SVN都是集中式的版本控制系统，而Git是分布式版本控制系统。

　　集中式版本控制系统，版本库是集中存放在中央服务器的，一起工作的人需要用自己的电脑从服务器上同步更新或上传自己的修改。
![banbenkongzhi](https://segmentfault.com/img/bVpR5z)

　但是，所有的版本数据都存在服务器上，用户的本地设备就只有自己以前所同步的版本，如果不连网的话，用户就看不到历史版本，也无法切换版本验证问题，或在不同分支工作。。

　　而且，所有数据都保存在单一的服务器上，有很大的风险这个服务器会损坏，这样就会丢失所有的数据，当然可以定期备份。

#分布式版本控制#
那分布式版本控制系统与集中式版本控制系统有何不同呢？

　分布式版本控制系统根本没有“中央服务器”，每个人的电脑上都是一个完整的版本库，不需要联网就可以工作。既然每个人电脑上都有一个完整的版本库，那多个人如何协作呢？比方说你和同事在各自电脑修改相同文件，这时，你们俩之间只需把各自的修改推送给对方，就可以互相看到对方的修改了。

　　分布式版本控制系统的安全性要高很多，因为每个人电脑里都有完整的版本库。大家之间可以相互复制。

　　分布式版本控制系统通常也有一台充当“中央服务器”的电脑，但这个服务器的作用仅仅是用来方便“交换”大家的修改，没有它大家也一样干活，只是交换修改不方便而已。

![fenbu](https://segmentfault.com/img/bVpR5A)

#安装Git#
　　最早Git是在Linux上开发的，很长一段时间内，Git也只能在Linux和Unix系统上跑。不过，慢慢地有人把它移植到了Windows上。现在，Git可以在Linux、Unix、Mac和Windows这几大平台上正常运行了。

　　在Linux上安装Git

　　首先，你可以试着输入git，看看系统有没有安装Git：

		$ git
　像上面的命令，有很多Linux会友好地告诉你Git没有安装，还会告诉你如何安装Git。

　　如果你碰巧用Debian或Ubuntu Linux，通过一条sudo apt-get install git就可以直接完成Git的安装，非常简单。如果想查看是否安装成功，通过git --version。

　　如果是其他Linux版本，可以直接通过源码安装。先从Git官网下载源码，然后解压，依次输入：./config，make，sudo make install这几个命令安装就好了。

　　安装完成后，还需要最后一步设置，在命令行输入：　　

		$ git config --global user.name "Your Name"
		 git config --global user.email "email@example.com"
因为Git是分布式版本控制系统，所以每个机器都必须自报家门：你的名字和Email地址。

　　注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。在此课程中，我们配置的环境中Git已安装好，我们课程提供也是在Linux系统中命令进行操作。

---

#什么是版本库？#
　版本库又名仓库，英文名repository，你可以简单理解成一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。

　　所以，创建一个版本库非常简单，首先，选择一个合适的地方，创建一个空目录：

		$ mkdir learngit
		$ cd learngit
		$ pwd
		/home/hubwiz/learngit
pwd命令用于显示当前目录。在环境中这个仓库位于/home/hubwiz/learngit。

　　通过git init命令把这个目录变成Git可以管理的仓库：

		$ git init
		Initialized empty Git repository in /home/hubwiz/learngit/.git/	
瞬间Git就把仓库建好了，而且告诉你是一个空的仓库（empty Git repository），细心的读者可以发现当前目录下多了一个.git的目录，这个目录是Git来跟踪管理版本库的，没事千万不要手动修改这个目录里面的文件，不然改乱了，就把Git仓库给破坏了。

　　如果你没有看到.git目录，那是因为这个目录默认是隐藏的，用ls -ah命令就可以看见。

---
#添加文件#
　　我们了解下版本控制系统，其实只能跟踪文本文件的改动，比如TXT文件，网页，所有的程序代码等等，Git也不例外。版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。而图片、视频这些二进制文件，虽然也能由版本控制系统理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是只知道图片从100KB改成了120KB，但到底改了啥，版本控制系统不知道，也没法知道。

　　为了简明起见，我们创建一个readme.txt作为练习：

		echo "Git is a version control system." > readme.txt
		// 输入这句话保存到创建的readme.txt文件中
		echo " Git is free software." >> readme.txt
		// 输入此内容追加到readme.txt中
　　一定要放到learngit目录下（子目录也行），因为这是一个Git仓库，放到其他地方Git再厉害也找不到这个文件。

　　用命令git add告诉Git，把文件添加到仓库：

		$ git add readme.txt
　　git add 实际上是个脚本命令，没有任何显示，说明添加成功。

----

#提交文件#
用命令git commit告诉Git，把文件提交到仓库：

		$ git commit -m "wrote a readme file"
		[master (root-commit) cb926e7] wrote a readme file
		1 file changed, 2 insertions(+)
		create mode 100644 readme.txt
　简单解释一下git commit命令，-m后面输入的是本次提交的说明，可以输入任意内容，当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录。

　　git commit命令执行成功后会告诉你，1个文件被改动（我们新添加的readme.txt文件），插入了两行内容（readme.txt有两行内容）。

　　为什么Git添加文件需要add，commit一共两步呢？因为commit可以一次提交很多文件，所以你可以多次add不同的文件，比如：
		$ git add file1.txt
		$ git add file2.txt file3.txt
		$ git commit -m "add 3 files."
