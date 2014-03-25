from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

# router = routers.DefaultRouter()
# router.register(r'item', views.ItemViewSet)
# router.register(r'category', views.CategoryViewSet)
# router.register(r'list', views.ItemListViewSet)
# router.register(r'users', views.UserViewSet)

urlpatterns = patterns('core.views',
#    url(r'^', include(router.urls)),
    url(r'^l/$', 'itemlist_list'),
    url(r'^l/(?P<pk>[0-9]+)$', 'itemlist_detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)
