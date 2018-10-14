# 学习日志
在这里我会记录我碰到的一些问题。
本日志会按照时间进行排序。
## 20181014
### 创建Django项目

### 启动测试web服务器
Edmond:mysite edmond$ python manage.py runserver 0:8888
  File "manage.py", line 14
    ) from exc
         ^
SyntaxError: invalid syntax
上面这个语句有两个地方出错，首先python需要使用python3（mac下3.7使用命令python3，pip使用pip3）
根据Stack Overflow查询到的信息，编辑manage.py文件，删除from exc后再次运行，成功。
Stack Overflow地址：https://stackoverflow.com/questions/47880626/django-manage-py-runserver-invalid-syntax
### 添加urls
良心建议，仔细看教程。。。不要跳来跳去。。。
不然属于自己挖坑自己填。。。
### 数据库配置
