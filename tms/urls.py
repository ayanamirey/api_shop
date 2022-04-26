from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tms.views import CategoryList, ProductListViewSet

router = DefaultRouter()
router.register('category', CategoryList, basename='CategoryList')
router.register('product', ProductListViewSet, basename='ProductListViewSet')

urlpatterns = [
    path('', include(router.urls))
]
