from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from application.api.reousrces import ApplicationResource, PaymentResource

v1_api = Api(api_name='v1')
v1_api.register(ApplicationResource())
v1_api.register(PaymentResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SchoolMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls))
)
