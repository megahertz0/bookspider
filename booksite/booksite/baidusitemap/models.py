#coding:utf-8
from django.contrib.sites.models import Site
from django.core import paginator
from django.core.exceptions import ImproperlyConfigured
try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:     # Python 2
    from urllib import urlencode, urlopen

class BaiduSitemap(object):
    # This limit is defined by Google. See the index documentation at
    # http://sitemaps.org/protocol.php#index.
    limit = 50000

    # If protocol is None, the URLs in the sitemap will use the protocol
    # with which the sitemap was requested.
    protocol = None

    def __get(self, name, obj, default=None):
        try:
            attr = getattr(self, name)
        except AttributeError:
            return default
        if callable(attr):
            return attr(obj)
        return attr

    def items(self):
        return []

    def location(self, obj):
        return obj.get_absolute_url()

    def _get_paginator(self):
        return paginator.Paginator(self.items(), self.limit)
    paginator = property(_get_paginator)

    def get_urls(self, page=1, site=None, protocol=None):
        # Determine protocol
        if self.protocol is not None:
            protocol = self.protocol
        if protocol is None:
            protocol = 'http'

        # Determine domain
        if site is None:
            if Site._meta.installed:
                try:
                    site = Site.objects.get_current()
                except Site.DoesNotExist:
                    pass
            if site is None:
                raise ImproperlyConfigured("To use sitemaps, \
                    either enable the sites framework or pass \
                    a Site/RequestSite object in your view.")
        domain = site.domain

        urls = []

        for item in self.paginator.page(page).object_list:
            loc = "%s://%s%s" % (
                protocol, domain, self.__get('location', item))
            priority = self.__get('priority', item, None)
            url_info = {
                'item':       item,
                'location':   loc,
                'lastmod':    self.__get('lastmod', item, None),
                'changefreq': self.__get('changefreq', item, None),
                'priority':   str(
                    priority is not None and priority or '')
            }
            if hasattr(self, 'wml_url'):
                url_info['wml_url'] = "%s://%s%s" % (
                    protocol, domain, self.__get('wml_url', item))
            if hasattr(self, 'xhtml_url'):
                url_info['xhtml_url'] = "%s://%s%s" % (
                    protocol, domain, self.__get('xhtml_url', item))
            if hasattr(self, 'html_url'):
                url_info['html5_url'] = "%s://%s%s" % (
                    protocol, domain, self.__get('xhtml_url', item))
            urls.append(url_info)
        return urls