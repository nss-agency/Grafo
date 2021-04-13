from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns

from core import views

urlpatterns = i18n_patterns(
    path('dev/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('works/', views.works, name='works'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    re_path(r'work/(?P<slug>[\w-]+)/$', views.work, name='work'),
    path(r'tinymce/', include('tinymce.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
