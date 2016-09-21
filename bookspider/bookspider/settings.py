# -*- coding: utf-8 -*-
# Scrapy settings for bookspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os
import sys
import booksite
from django.core.wsgi import get_wsgi_application

LOG_ENABLED = False

# reload(sys)
# sys.setdefaultencoding('utf-8')
sys.path.append(os.path.dirname(booksite.__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'booksite.settings'
from django.conf import settings as djsettings

application = get_wsgi_application()

BOT_NAME = 'bookspider'

SPIDER_MODULES = ['bookspider.spiders']
NEWSPIDER_MODULE = 'bookspider.spiders'

REDIRECT_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookspider (+http://www.yourdomain.com)'

IMAGES_STORE = os.path.join(djsettings.MEDIA_ROOT, 'bookimgs')

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'bookspider.pipelines.BookinfoPipeline': 300,
    'bookspider.pipelines.BookpagePipeline': 300,
    'bookspider.pipelines.QidianRankPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'bookspider.middlewares.ProxyMiddleware': 100,
    'bookspider.middlewares.RotateUserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware':350,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
}

PROXY_LIST = [
#    "111.13.55.3:22",

]

DNSCACHE_ENABLED = True
DEPTH_LIMIT = 6
DEPTH_PRIORITY = 1
DOWNLOAD_TIMEOUT=30
DOWNLOAD_MAXSIZE = 3 * 1024 * 1024

try:
    from .local_settings import *
except:
    raise ImportError('应当使用与settings同级别目录下的local_settings文件')
