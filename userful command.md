### 启动测试服务器
python3 manage.py runserver
### migrate迁移数据
python3 manage.py migrate
### 检测模型文件的修改
python3 manage.py makemigrations polls
### django生成SQL
python3 manage.py sqlmigrate polls 0001
                             apps名
### 当发现migrate前定义错了model，需要重新migrate时
1.删除db内django_migrations表内数据
2.删除项目文件夹下migrationd文件夹内所有文件。
3.重新进行makemigrations和migrate
