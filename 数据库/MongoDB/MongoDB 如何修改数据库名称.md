### 一.通过copy再删除

```
db.copyDatabase('old_name', 'new_name'); 
use old_name 
db.dropDatabase();
```
### 二.通过移动集合来修改数据库名

```
 use admin;
 db.adminCommand({renameCollection: "test.test", to: "test1.test"});
```
当你把所有的集合移动到了新的库下，就相当于把整个库重命名了。这会比copyDatabase快很多。
虽然MongoDB没有renameDatabase的命令，但提供了renameCollection的命令，这个命令并不是仅仅能修改collection的名字，同时也可以修改database。