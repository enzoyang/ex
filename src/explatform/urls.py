from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
                      # (r'^Register/$', 'explatform.account.views.Register'),
    # Example:
    # (r'^explatform/', include('explatform.foo.urls')),

    # Uncomment this for admin:
(r'^admin/', include(admin.site.urls)),
)
