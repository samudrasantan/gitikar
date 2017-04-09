"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from mysite import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'album.views.search_page'),
    url(r'^search/$', 'album.views.search_page'),
    url(r'^list/$', 'album.views.alphabet_list'),
    url(r'^list/(?P<alf>[\w|\W]+)/$', 'album.views.list_results', name='alphabet_list'),
    url(r'^gaan/(?P<username>[\w|\W]+)/$', 'album.views.gaa_go'),
    url(r'^album/(?P<username>[\w|\W]+)/$', 'album.views.album_go'),
    url(r'^gitikar/(?P<username>[\w|\W]+)/$', 'album.views.git_go'),
    url(r'^catagory/(?P<username>[\w|\W]+)/$', 'album.views.cat_go'),
    url(r'^prokashok/(?P<username>[\w|\W]+)/$', 'album.views.publisher_album_list'),
     url(r'^year/(?P<username>[\w|\W]+)/$', 'album.views.publisher_album_list'),
    url(r'^shilpi/(?P<username>[\w|\W]+)/$', 'album.views.artist_activity'),
    url(r'^band/(?P<username>[\w|\W]+)/$', 'album.views.ban_go'),
    url(r'^album_details/(?P<username>[\w|\W]+)/$', 'album.views.album_details'),
    url(r'^band_details/(?P<username>[\w|\W]+)/$', 'album.views.band_details'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
