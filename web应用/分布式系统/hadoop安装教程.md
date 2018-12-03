#hadoop安装教程（CentOs 7.4 + jdk1.8.0_141 + hadoop-3.0.0）
###hadoop伪分布式安装
1. 新建一个用户，为用户添加权限
2. 安装SSH，配置SSH免密码登录（默认安装）

 		现在先确认能否不输入口令就用ssh登录localhost:
		ssh localhost
		
		如果不输入口令就无法用ssh登陆localhost，执行下面的命令：
		ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
		cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys 
3. 下载 jdk1.8.0_141 解压到  /usr/local/java 

		如果没有此目录请预先创建
		下载： wget http://mirrors.linuxeye.com/jdk/jdk-8u141-linux-x64.tar.gz
		解压： tar -zxvf jdk-8u141-linux-x64.tar.gz -C /usr/local/java

		设置环境变量：
		vim /etc/profile

		添加以下内容：
		#set java environment
		export JAVA_HOME=/usr/java/jdk1.8.0_141
		export CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib
		export PATH=$JAVA_HOME/bin:$PATH

		按 Esc 键退出编辑模式，输入 :wq 保存并关闭文件。
		加载环境变量：source /etc/profile

		查看 jdk 版本
		java -version   （当出现 jdk 版本信息时，表示 JDK 已经安装成功如以下内容）

		java version "1.8.0_141"
		Java(TM) SE Runtime Environment (build 1.8.0_141-b15)
		Java HotSpot(TM) 64-Bit Server VM (build 25.141-b15, mixed mode)
4. 下载 hadoop-3.0.0 解压到 /usr/local/hadoop

		下载： wget http://mirror.bit.edu.cn/apache/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz
		解压： tar -zxvf hadoop-3.0.0.tar.gz -C /usr/local/hadoop

		设置环境变量：
		vim ~/.bashrc

		添加以下内容
		# Hadoop Environment  Variables
		export HADOOP_HOME=/usr/local/hadoop/hadoop-3.0.0
		export HADOOP_INSTALL=$HADOOP_HOME
		export HADOOP_MAPRED_HOME=$HADOOP_HOME
		export HADOOP_COMMON_HOME=$HADOOP_HOME
		export HADOOP_HDFS_HOME=$HADOOP_HOME
		export YARN_HOME=$HADOOP_HOME
		export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
		export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin

		按 Esc 键退出编辑模式，输入 :wq 保存并关闭文件。
		加载环境变量：source ~/.bashrc

		检查hadoop是否安装完毕
		hadoop version

5. hadoop 伪分布式主要设置


	- 往文件 core-site.xml 中的`<configuration>`添加以下内容：

	        <property>
	                <name>fs.defaultFS</name>
	                <value>hdfs://localhost/</value>
	        </property>

	-  往文件 hdfs-site.xml 中的`<configuration>`添加以下内容：
 
			<property>
                <name>dfs.replication</name>
                <value>1</value>
        	</property>
	-  往文件 mapred-site.xml 中的`<configuration>`添加以下内容：

	        <property>
                <name>mapreduce.framework.name</name>
                <value>yarn</value>
        	</property>
	-  往文件 yarn-site.xml 中的`<configuration>`添加以下内容：

	        <property>
                <name>yarn.resourcemanager.hostname</name>
                <value>localhost</value>
        	</property>
        	<property>
                <name>yarn.nodemanager.aux-services</name>
                <value>mapreduce_shuffle</value>
        	</property>
	-  修改 hadoop-env.sh 文件添加 JAVA_HOME：
 
			export JAVA_HOME=/usr/local/java

6. 格式化一个新的分布式文件系统：

		hadoop namenode -format
7. 启动Hadoop守护进程：

		start-all.sh
8. 查看守护进程是否正在运行：

		jps
		也可以通过打开网页来查看（新旧版本端口号不一样）
		http://localhost:50070    查看namenode		
		http://localhost:8088     查看资源管理器	
		


# hadoop-3.0新特性 #

	要求jdk版本不低于1.8， 对默认端口进行了修改

	Namenode ports: 50470 --> 9871, 50070--> 9870, 8020 --> 9820
	
	Secondary NN ports: 50091 --> 9869,50090 --> 9868
	
	Datanode ports: 50020 --> 9867, 50010--> 9866, 50475 --> 9865, 50075 --> 9864
	
	Kms server ports: 16000 --> 9600 (原先的16000与HMaster端口冲突)



##注意事项：
免密码登录可能会出现， 依然需要密码， 这种状态

解决方案：

用root用户登陆 查看系统的日志文件：

	tail /var/log/secure -n 20
如果提示/home/hadooper/.ssh和 /home/hadooper/.ssh/authorized_keys权限不对，修改如下：   

	chmod 700 ~/.ssh
	chmod 600 ~/.ssh/authorized_keys 

<font color=#F00 size=12 face="黑体">修改环境变量时一定要注意修改的是谁的环境变量</font>



# hadoop完全分布式
##修改6个配置文件 core-site.xml，hdfs-site.xml，mapred-site.xml，yarn-site.xml， workers， yarn-env.sh
###修改core-site.xml

	<configuration>
	 <!-- 指定HDFS老大（namenode）的通信地址 -->
	    <property>
	        <name>fs.defaultFS</name>
	        <value>hdfs://Master:9000</value>
	    </property>
        <property>
                <name>hadoop.tmp.dir</name>
                <value>/home/zhang/tmp</value>
                <description>Abase for other temporary directories.</description>

        </property>
	</configuration>


###修改hdfs-site.xml

	<configuration>
	 <!-- 设置hdfs副本数量 -->
	    <property>
	        <name>dfs.replication</name>
	        <value>3</value>
	    </property>
        <property>
                <name>dfs.namenode.name.dir</name>
                <value>/home/zhang/hdfs/name</value>
        </property>
	    <property>
                <name>dfs.datanode.data.dir</name>
                <value>/usr/local/hadoop/zhang</value>
        </property>
	    <property>
                <name>dfs.namenode.secondary.http-address</name>
                <value>Master:9868</value>
        </property>
	
	</configuration>

###修改mapred-site.xml
	<configuration>
	
	    <property>
	        <name>mapreduce.framework.name</name>
	        <value>yarn</value>
	    </property>
	    <property>
	        <name>mapreduce.jobhistory.address</name>
	        <value>Master:10020</value>
	    </property>
	    <property>
	        <name>mapreduce.jobhistory.webapp.address</name>
	        <value>Master:19888</value>
	    </property>
	
	</configuration>


###修改yarn-site.xml
	<configuration>

	<!-- Site specific YARN configuration properties -->
	
	    <property>
	        <name>yarn.nodemanager.aux-services</name>
	        <value>mapreduce_shuffle</value>
	    </property>
	    <property>
	        <name>yarn.resourcemanger.hostname</name>
	        <value>Master</value>
	    </property>
	</configuration>
	                  
###修改workers
	填写主机名（一行一个）
###修改yarn-env.xml
	添加   JAVA_HOME环境   如
	export JAVA_HOME=/usr/local/java/jdk1.8.0_141




##注意事项
<font color=#F00 size=6 face="黑体">可能会出现找不到datanode的情况查看log发现是缺少权限，当加上最高权限还是不行时，请找一个当前用户权限允许的位置建文件夹。。。
默认是新建用户在进行操作，当用root用户是会报错你需要再加配置</font>