"""ajax_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from books import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
	url(r'^(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^create/$', views.book_create, name='book_create'),
    url(r'^$', views.book_list, name='book_list'),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
