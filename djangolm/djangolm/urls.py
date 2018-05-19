from django.conf.urls import include, url
from django.contrib import admin
from boletin import views
# from boletin.views inicio

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangolm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio, name='inicio')
]
