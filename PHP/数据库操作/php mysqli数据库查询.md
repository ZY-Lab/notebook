#php 使用mysqli连接MySQL数据库查询操作
#####1、mysqli_connect(host,username,password,dbname,port,socket);

参数 | 描述
- | :-: 
host| 可选。主机名或 IP 地址。
username | 可选。MySQL 用户名。
password | 	可选。MySQL 密码。
dbname | 	可选。MySQL数据库名称
port | 	可选。MySQL 服务器的端口号。
socket | 可选。socket 或要使用的已命名 pipe。


返回值： 返回一个代表到 MySQL 服务器的连接的对象。

#####2、mysqli_query(connection,query,resultmode);

参数 | 描述
- | :-: 
connection| 必需。使用的 MySQL 连接对象。
query | 必需，SQL语句
resultmode | 	可选。一个常量。可以是下列值中的任意一个：MYSQLI_USE_RESULT（如果需要检索大量数据，请使用这个），MYSQLI_STORE_RESULT（默认）

返回值：	查询语句会返回一个结果集，其他返回True，False


#####3、mysql_fetch_array(data,array_type)

参数 | 描述
- | :-: 
data| 可选。 mysql_query() 函数产生的结果。
array_type | 可选。规定返回哪种结果。可能的值：MYSQL_ASSOC - 关联数组，MYSQL_NUM - 数字数组，MYSQL_BOTH - 默认。同时产生关联和数字数组

关联数组：{'a':'b'},下标为非数字的数组
数字数组：{'1':'b}，下标为数字的数组

返回值： 查询结果的数组形式

##实例
	$con = mysqli_connect("localhost", "root", "root", "transport_system");
	$strsql = "SELECT * FROM auth_user";
	$result = mysqli_query($con, $strsql);
	print_r($result->fetch_array(MYSQL_ASSOC));

##结果
	Array ( 
    [id] => 3 [password] => pbkdf2_sha256$36000$WZXxdxA8tTvi$jNEXQzR6cHPB3CwkoO6rj9MAbf+yNvPnzLYH0WZ5EkY= 
    [last_login] => 2018-01-18 02:48:22 
    [is_superuser] => 1 
    [username] => admin 
    [first_name] => 
    [last_name] => 
    [email] => q@qq.com 
    [is_staff] => 1 
    [is_active] => 1 
    [date_joined] => 2018-01-18 02:48:13 )