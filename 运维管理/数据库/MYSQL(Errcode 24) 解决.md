## MYSQL(Errcode 24) 解决


出现Out of resources when opening file './xxx.MYD' (Errcode: 24)错误是因为打开的文件数超过了my.cnf的--open-files-limit。open-files-limit选项无法在mysql命令行直接修改，必须在my.cnf中设定，最大值是65536。

    my.cnf里如果配置了open_files_limit，则open_files_limit最后取值为 配置文件 open_files_limit，max_connections*5， wanted_files= 10+max_connections+table_cache_size*2 三者中的最大值。

    如果my.cnf里如果没配置open_files_limit，
    则open_files_limit最后取值为max_connections*5，10+max_connections+table_cache_size*2，ulimit -n中的最大者

重启mysql:
> service mysqld restart