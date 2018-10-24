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
今日未进行。
## 20181021
### 启动django时报错不存在django
因mac上同时存在2.7和3.6两个python，在terminal中执行python manage.py runserver 时需要特别注意python是哪一个版本。根据环境变量，mac上python命令启动python2.7，所以此处需要使用python3命令。
### django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
pip install pymysql后没有导入，需要在项目__init__.py中导入以下命令
import pymysql
pymysql.install_as_MySQLdb()
### 一个要认真仔细看的错误信息
输出内容为：
>>> q=Question(question_text="whats new?", pub_date=timezone.now())
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/usr/local/lib/python3.6/site-packages/django/db/models/base.py", line 485, in __init__
    raise TypeError("'%s' is an invalid keyword argument for this function" % kwarg)
TypeError: 'question_text' is an invalid keyword argument for this function

此时检查polls/models.py文件，发现原书写内容为：
>>> class Question(models.Model):
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_test

可见Question类只有question_test这个变量，没有question_text变量。
所以，在python3 manage.py shell里，输入q = Question(question_text="What's new?", pub_date=timezone.now())会报错，但是用q.question_text="XXXXXX"方式能够正确执行但是无法再数据库内被写入的原因是，shell中执行的q.question_text被python认为是一次变量新增，但是这个变量并没有被migrate到mysql 里面，所以数据库并不会记录这个新增的变量变化情况。
切记要仔细！
## 20181024
### 今天尝试改为oracle驱动，试试看！
成功，没有出现任何问题。
结合朋友碰到的问题，汇总一下
1.django版本与python版本要配合。
    django2.1 python3.6
2.django版本与oracle版本要配合。
    django2.1 oracle12c+
3.如要使用oracle11g，需要降低django版本到1.11
### 视图的理解
>>> from django.http import HttpResponse
from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
 # Leave the rest of the views (detail, results, vote) unchanged

Question.objects.order_by('-pub_date')[:5]中的[:5]用途为返回order by之后的前5个纪录。
output变量为list，每个变量用逗号隔开，拼接问题list中的值。
