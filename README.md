# Book Spider #

## 概况 ##

1. 包含一个Scrapy爬虫项目
2. 包含一个Django站点, 用来显示书籍
3. 爬虫与站点的数据模型相关联
4. 爬虫实现了以下站点的内容收集:

| 网站域名          | 爬虫名称 |
|-------------------|----------|
| www.86696.cc      | douluo   |

5. 站点已完成功能:
> * 用户登录
> * 用户书架
> * 书籍书签的增加与删除
> * 手机端样式的适配
> * 按书籍名称搜索
> * 按作者浏览
> * 分类浏览
> * 排行榜
>> * 点击排行
>> * 收藏排行

6. 未完成事项:
> * 书目整理
> * 评论系统
> * 投票系统
> * 排行榜
>> * 推荐排行
> * 书籍更新内容获取方式

## 安装使用 ##

1. 安装Python 2.7
1. 安装Pip
1. 使用pip安装Scrapy Django
1. clone本项目
1. `cd booksite && python setup.py develop`
1. 配置Django项目的 `local_settings.py` 文件,位于:`PROJECT_DIR/booksite/booksite`,配置数据库, 如:

```
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'bookspider',
			'USER': 'spider',
			'PASSWORD': 'admin',
			'HOST': '127.0.0.1',
		}
	}
```
1. 生成数据库 `python manage.py syncdb`
1. 进入目录 `PROJECT_DIR/bookspider`
1. 使用Scrapy进行抓取, `scrapy crawl "爬虫名称"`

### ubuntu ###
django-1.10.1 python 2.7.12

1. sudo apt-get install python-pip
1. sudo apt-get install python-dev python3-dev libxml2-dev libxslt1-dev zlib1g-dev
1. sudo apt-get install libffi-dev
1. sudo pip install scrapy
1. sudo pip install django
1. sudo pip install raven
1. sudo pip install celery
1. sudo pip install django_assets
1. sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev  libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
1. sudo apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev
1. sudo pip install redis
1. sudo pip install django-redis
1. sudo apt-get install libpq-dev
1. sudo pip install psycopg2
1. sudo pip install django_pgjson
1. sudo pip install  django-simple-captcha
1. sudo pip install PyQuery
1. install new redis server 3.x http://redis.io/download
1. sudo pip install redis_cache
1. sudo pip install redis-simple-cache
1. python manage.py makemigrations
1. python manage.py migrate
1. python manage.py collectstatic
1. sudo pip install scrapy_djangoitem
1. sudo pip install cssutils
1. sudo pip install pyjade
1. modify pyjade  https://github.com/syrusakbary/pyjade/pull/263/commits/9bfc036c96ff9d9908d6b6c0016a3097e11a91db
1. install scrapyd & deploy
	1. pip install scrapyd
	2. pip install scrapy-client
	3. cd bookspider
	4. scrapyd-deploy
	5. run spider in scrapyd with http and curl
1. gunicorn+gevet
	1. pip install gunicorn
	1. pip install greenlet
	1. pip install eventlet
	1. pip install gevent
	1. pip install supervisor
