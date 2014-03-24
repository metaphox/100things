from django.conf.urls import patterns, url, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'list', views.ItemListViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
