from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^Register/$','explatform.account.views.Register'),
    # Example:
    # (r'^explatform/', include('explatform.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
