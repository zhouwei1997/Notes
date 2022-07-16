[TOC]

# 数据库操作的SQL

1、查看所有数据库

~~~sql
show databases;
~~~

2、创建数据库

~~~SQL
create database 数据库名 charset=utf8mb4;
create database python charset=utf8mb4;
~~~

3、删除数据库

~~~sql
drop database 数据库名;
drop database python;
~~~

4、查看当前使用的数据库

~~~sql
select database();
~~~

# 表结构操作sql语句

1、创建表

~~~SQL
create table student(
	id int unsigned primary key auto_increment not null,
    name varchar(20) not null,
    age tinyint unsigned default 0;
    height decimal(5,2);
    gender enum('男','女','保密')
);
~~~

2、添加表字段

~~~SQL
alter table 表名 add 列名 类型 约束;
alter table student
~~~

3、修改字段类型

~~~SQL
alter table 表名 modify 列名 类型 约束;
alter table student modify birthday date not null;
~~~

> modify：只能修改字段类型或者约束，不能修改字段名

4、修改字段名和字段类型

~~~SQL
alter table 表名 change 原名 新名 类型及约束;
alter table students change birthday birth datetime not null;
~~~

> change：既能对字段重命名又能修改字段类型还能修改约束

5、删除字段

~~~SQL
alter table 表名 drop 列名;
alter table students drop birthday;
~~~

6、删除表

~~~SQL
drop table 表名;
drop table students;
~~~

# 表操作SQL语句

1、查询数据

~~~SQL
# 查询所有列
select * from 表名;
select * from student;
# 查询指定的列
select 列1,列2... from 表名;
select id,name from student;
~~~

2、添加数据

~~~SQL
# 全列插入：值的顺序和表结构字段的顺序完全一一对应
insert into 表名 values (...)
insert into students values(0,'zhangsan',default,default,'男');
# 部分值插入：值的顺序与给出的列顺序对应
insert into 表名 (列1,...) values (值1，...)
insert into students(name,age) values('zhangsan',15);
# 全列多行插入
insert into 表名 values (...),(...)...
insert into students values(0,'zhangsan',default,default,'男'),(0,'lisi',58,185,'男');
# 部分列多行插入
insert into 表名 (列1,...) values (值1，...),(值1，...)...
insert into students(name,age) values('zhangsan',15),('wangwu',25);
~~~

> - 主键列是自增长，但是全列插入时需要占位，通常使用空值（0或null或default）
> - 在全列插入时，如果字段列有默认值可以使用default来占位，插入后的数据就是之前设置的默认值

3、修改数据

~~~SQL
update 表名 set 列1=值1，列2=值2...where 条件
update students set age = 25,gender = '女' where name = 'zhangsan';
~~~

4、删除数据

~~~SQL
delete from 表名 where 条件;
delete from student where id = 5;
~~~

删除数据还可以使用逻辑删除，添加一个标识字段，删除的时候是将该标识字段的状态进行改变即可

~~~SQL
alter table students add is_del tinyint default 0;
~~~

# distinct关键字

distinct可以去除重复的数据行

~~~SQL
select distinct 列1,... from 表名
# 查询班级中学生的姓名
select distinct name,gender from students;
~~~

# 连接查询

连接查询可以实现多个表的查询，当查询的字段数据来自不同的表就可以使用连接查询来完成

## 内连接查询

查询两个表中符合条件的共有记录

![image-20220715101752689](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207151017777.png)

~~~SQL
select 字段 from 表1 inner join 表2 on 表1.字段1 = 表2.字段2
select * from student as s inner join classes as c s.cls_id = c.id;
~~~

> - inner join 就是内连接查询关键字
> - on 就是连接查询条件

## 左连接查询

以左表为主根据条件查询右表数据，如果根据条件查询右表数据不存在使用null值填充

![image-20220715110202233](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207151102295.png)

~~~SQL
select 字段 from 表1 left join 表2 on 表1.字段 = 表2.字段2;
select * from students as s left join classes as c on s.cls_id = c.id;
~~~

## 右连接查询

以右表为主根据条件查询左表数据，如果根据条件查询数据不存在使用null值填充

![image-20220715110547168](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207151105236.png)

~~~SQL
select 字段 from 表1 right join 表2 on 表1.字段1 = 表2.字段2;
select * from students as s right join classes as c on s.cls_id = c.id;
~~~

## 自连接查询

左表和右表是同一个表，根据连接查询条件查询两个表中的数据

![image-20220715110825860](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207151108995.png)

# 子查询

在一个select语句中，嵌入了另一个select语句，那么被嵌入的select语句称之为子查询，外部那个select语句则称为主查询

## 主查询和子查询的关系

- 子查询是嵌入到主查询中
- 子查询是辅助主查询的，要么充当条件，要么充当数据源
- 子查询是可以单独存在的语句，是一条完整的select语句

~~~sql
# 查询大于平均年龄的学生
select * from students where age > (select avg(age) from students);
# 查询学生在班级的所有班级名称
select name from classes where id in (select cls_id from students where cls_id is not null);
# 查找年龄最大，身高最高的学生
select * from students where (age,height) = (select max(age),max(height) from students);
~~~

#  外键

外键约束：对外键字段的值进行更新和插入时会引用表中字段的数据进行验证，数据如果不合法则更新和插入会失败，保证数据的有效性

## 对已存在的字段添加外键约束

~~~SQL
-- 为cls_id字段添加外键约束
alter table students add foreign key(cls_id) references classes(id);
~~~

## 在创建数据表时创建外键

~~~SQL
-- 创建学校表
CREATE TABLE school(
  id INT NOT NULL PRIMARY key auto_increment,
  name VARCHAR(10)
);

-- 创建老师表
CREATE TABLE teacher(
  id INT NOT NULL PRIMARY key auto_increment,
  name VARCHAR(10),
  s_id INT NOT NULL,
  FOREIGN key(s_id) REFERENCES school(id)
);
~~~

## 删除外键索引

~~~SQL
-- 根据名称来删除外键约束
ALTER TABLE
  teacher DROP foregin key s_id;
~~~





