# -*- coding: utf-8 -*-

import urllib2
import lxml
from lxml import etree

data = urllib2.urlopen('http://www.proxy360.cn/default.aspx').read()

tree=etree.HTML(data)
nodes=tree.xpath("/html/body/form/div/table/tr/td/div/div[@name='list_proxy_ip']")
##nodes=tree.xpath("//div/span")
for node in nodes:
    items = node.xpath("div/span")
    print items[0].text.strip() + ":" + items[1].text.strip()

