# -*- coding: utf-8 -*-
# from django.views.generic.base import TemplateView
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from booksite.usercenter.views import ChangePWDView
from booksite.sitemap import BookSitemaps
import booksite
import django
from booksite.book.views import mb_index
from booksite.background.views import index

admin.autodiscover()

usercenter_urls = [
                           url(r'^bookmark/$', booksite.usercenter.views.bookmark, name='bookmark'),
                           url(r'^bookmark/(?P<bookmark_id>\d+)/read/(?P<page_number>\d+)/$',
                               booksite.usercenter.views.bookmark_read, name='bookmark_read'),
                           url(r'^bookmark/add/$', booksite.usercenter.views.add_bookmark, name='add_bookmark'),
                           url(r'^bookmark/(?P<bookmark_id>\d+)/delete/$', booksite.usercenter.views.del_bookmark, name='del_bookmark'),
                           url(r'^changepwd/$', ChangePWDView.as_view(), name='changepwd'),
                           ]

html5_urls = [
                      url(r'^$', mb_index, name='mb'),
                      url(r'^load/$', booksite.book.views.mb_load, name='mb_load'),
                      url(r'^search/$', booksite.book.views.mb_search, name='mb_search'),
                      url(r'^searchload/$', booksite.book.views.mb_searchload, name='mb_searchload'),
                      url(r'^login/$', booksite.usercenter.views.mb_login, name='mb_login'),
                      url(r'^logout/$', booksite.usercenter.views.mb_logout, name='mb_logout'),
                      url(r'^bookmark/$', booksite.usercenter.views.mb_bookmark, name='mb_bookmark'),
                      url(r'^book/(?P<book_id>\d+)/$', booksite.book.views.mb_bookindex, name='mb_bookindex'),
                      url(r'^page/(?P<page_number>\d+)/$', booksite.book.views.mb_bookpage, name='mb_bookpage'),
                      ]

background_urls = [
                           url(r'^$', index, name="home"),
                           url(r'^replace/$', booksite.background.views.replace, name="replace"),
                           url(r'^replace/delete/(?P<pk>\d+)/$', booksite.background.views.delete_rule, name="delete_rule"),
                           url(r'^replace/edit/(?P<pk>\d+)/$', booksite.background.views.edit_rule, name="edit_rule"),
                           url(r'^replace/apply/(?P<pk>\d+)/$', booksite.background.views.apply_rule, name="apply_rule"),
                           url(r'^replace/page/$', booksite.background.views.replace_page, name="replace_page"),
                           url(r'^replace/book/$', booksite.background.views.replace_book, name="replace_book"),
                           url(r'^tuijian/$', booksite.background.views.tuijian, name="tuijian"),
                           url(r'^tuijian/create/fengtui/$', booksite.background.views.fengtui_create, name="fengtui_create"),
                           url(r'^tuijian/create/jingtui/$', booksite.background.views.jingtui_create, name="jingtui_create"),
                           url(r'^tuijian/delete/(?P<model>ft|jt)/(?P<book_id>\d+)/$',
                               booksite.background.views.del_tuijian, name="del_tuijian"),
                           url(r'^booksearch/$', booksite.background.views.book_search, name="book_search"),
                           url(r'^booksearch/jx/$', booksite.background.views.book_jx, name="book_jx"),
                           url(r'^booksearch/ft/$', booksite.background.views.book_ft, name="book_ft"),
                           url(r'^booksearch/jt/$', booksite.background.views.book_jt, name="book_jt"),
                           url(r'^booksearch/jxall/$', booksite.background.views.book_jiuzhenggengxin, name="book_jiuzhenggengxin"),
                           url(r'^booksearch/pagezipper/$', booksite.background.views.book_page_next_zipper, name="book_page_next_zipper"),
                           url(r'^newbook/$', booksite.background.views.get_new_book, name="newbook"),
                           ]

password_reset_urls = [
                               url(r'^$',
                                   django.contrib.auth.views.password_reset,
                                   {
                                       'template_name': 'usercenter/password_reset_form.jade',
                                       'email_template_name': 'usercenter/password_reset_email.html',
                                   },
                                   name='password_reset'
                                   ),
                               url(r'^done/$',
                                   django.contrib.auth.views.password_reset_done,
                                   {'template_name': 'usercenter/password_reset_done.jade'},
                                   name='password_reset_done'
                                   ),
                               url(r'^confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                                   django.contrib.auth.views.password_reset_confirm,
                                   {'template_name': 'usercenter/password_reset_confirm.jade'},
                                   name='password_reset_confirm'
                                   ),
                               url(r'^complete/$',
                                   django.contrib.auth.views.password_reset_complete,
                                   {'template_name': 'usercenter/password_reset_complete.jade'},
                                   name='password_reset_complete'
                                   ),
                               ]

sitemaps = {
    'books': BookSitemaps,
}

urlpatterns = [
                       url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                           name='django.contrib.sitemaps.views.sitemap'),
                       # url(r'^sitemap\.xml$', 'booksite.baidusitemap.views.sitemap', {'sitemaps': sitemaps}, name='sitemap'),
                       url(r'^$', booksite.book.views.home, name='home'),
                       url(r'^fenlei/(?P<category>[a-z])/$', booksite.book.views.category, name='category'),
                       url(r'^bookrank/$', booksite.book.views.bookrank, name='bookrank'),
                       url(r'^booknews/$', booksite.book.views.booknews, name='booknews'),
                       url(r'^book/(?P<book_id>\d+)/$', booksite.book.views.bookindex, name='bookindex'),
                       url(r'^bookinfo/(?P<book_id>\d+)/$', booksite.book.views.bookinfo, name='bookinfo'),
                       url(r'^bookindex/(?P<book_id>\d+)/$', booksite.book.views.bookindexajax, name='bookindexajax'),
                       url(r'^page/(?P<page_number>\d+)/$', booksite.book.views.bookpage, name='bookpage'),

                       url(r'^nallpage/(?P<page_id>\d+)/$', booksite.book.views.load_nall_page, name='nallpage'),
                       url(r'^fixpic/page/(?P<page_id>\d+)/$', booksite.book.views.page_fix_pic, name='pagefixpic'),
                       url(r'^fixpic/book/(?P<book_id>\d+)/$', booksite.book.views.book_fix_pic, name='bookfixpic'),
                       url(r'^taskcheck/page/(?P<page_id>\d+)/$',
                           booksite.book.views.page_task_check, name='pagetaskcheck'),
                       url(r'^lineupdate/$', booksite.book.views.edit_line, name="lineupdate"),
                       url(r'^lineremove/(?P<page_id>\d+)/$', booksite.book.views.del_line, name="del_line"),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^usercenter/', include(usercenter_urls)),
                       url(r'^login/$', booksite.usercenter.views.login_view, name='login'),
                       url(r'^signup/$', booksite.usercenter.views.signup, name='signup'),
                       url(r'^logout/$', booksite.usercenter.views.logout_view, name='logout'),
                       url(r'^captcha/', include('captcha.urls')),

                       url(r'^resetpassword/', include(password_reset_urls)),

                       url(r'^mobile/', include(html5_urls)),

                       url(r'^bbg/', include(background_urls, namespace='bbg', app_name='booksite.background')),
                       ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
                            url(r'^media/book/(?P<path>.*)$', booksite.book.views.bookpage_zip, name='zippage')
                            ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
