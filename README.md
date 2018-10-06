## 说明
这是一个Flask模板，以后写flask项目可以直接套用

## Ecosystem

| Project | Status | Description |
|---------|--------|-------------|
| python          | 3.5.4 | 在这个版本以及以上都可以 |
| Flask    | 2.0.7 | 1.0.2 |

## 功能

```python
a. 增加 runserver
from chun import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app)

if __name__ == '__main__':
# app.run()
manager.run()


b. 位置传参
from chun import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app)

@manager.command
def custom(arg):
    """
自定义命令
python manage.py custom 123
:param arg:
:return:
"""
    print(arg)


    if __name__ == '__main__':
        # app.run()
        manager.run()
        
        
c. 关键字传参
from chun import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app)

@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def cmd(name, url):
    """
自定义命令
执行： python manage.py  cmd -n wupeiqi -u http://www.oldboyedu.com
:param name:
:param url:
:return:
"""
    print(name, url)


    if __name__ == '__main__':
        # app.run()
        manager.run()
        
3. flask-migrate 
pip3 install flask-migrate 
依赖：flask-script 

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sansa import create_app
from sansa import db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
Migrate(app, db)

"""
# 数据库迁移命名
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
"""
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    # app.run()
    
    
4. 找到项目使用的所有组件和版本。
pip install pipreqs

pipreqs ./ --encoding=utf-8 
```

## 用法

**python manage runserver -h 127.0.0.1 -p 8000**		指定IP和端口启动项目

**python manage.py db init**		数据库初始化

**python manage.py db migrate**	数据库读取

**python manage.py db upgrade**	数据库执行操作

还可以自定义执行命令