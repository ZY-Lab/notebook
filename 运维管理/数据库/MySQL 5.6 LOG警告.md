## MySQL 5.6 LOG警告

####MySQL 5.6 中TIMESTAMP with implicit DEFAULT value is deprecated错误

要关闭警告，需要加入下面的参数：

    [mysqld]
    explicit_defaults_for_timestamp=true
    
    重启MySQL后错误消失，这时TIMESTAMP的行为如下：
    •TIMESTAMP如果没有显示声明NOT NULL，是允许NULL值的，可以直接设置改列为NULL，而没有默认填充行为。
    •TIMESTAMP不会默认分配DEFAULT CURRENT_TIMESTAMP 和 ON UPDATE CURRENT_TIMESTAMP属性。
    •声明为NOT NULL且没有默认子句的TIMESTAMP列是没有默认值的。往数据表中插入列，又没有给TIMESTAMP列赋值时，如果是严格SQL模式，会抛出一 个错误，如果严格SQL模式没有启用，该列会赋值为'0000-00-00 00:00:00′，同时出现一个警告。（这和MySQL处理其他时间类型数据一样，如DATETIME）
    
    
####MySQL 5.6 中Changed limits: max_open_files: 1024 警告
除了修改/etc/security/limits.conf 加上

    * hard nofile 65535  
    * soft nofile 65535  

还需要在  /usr/lib/systemd/system/mysqld.service 加上

    LimitNOFILE=65535
    