"""acidbro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

from pages.views import TemplateAdminAJAXView, IndexView


urlpatterns = i18n_patterns(
    re_path(r'^$', IndexView.as_view(), name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^admin/', admin.site.urls),
    # extra url for fetching template
    path('template/fetch/<slug:text>/',
         TemplateAdminAJAXView.as_view()),

    path('', include('pages.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
)
