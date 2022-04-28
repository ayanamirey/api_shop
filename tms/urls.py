from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tms.views import CategoryList, ProductListViewSet, CartViewsSet, AddCart

router = DefaultRouter()
router.register('category', CategoryList, basename='CategoryList')
router.register('product', ProductListViewSet, basename='ProductListViewSet')
router.register('cart', CartViewsSet, basename='CartViewsSet')
router.register('add_to_cart', AddCart, basename='AddCart')

urlpatterns = [
    path('', include(router.urls)),
    # path('add/', AddCart.as_view({'create': 'create'}))
    # path('category/', CategoryList.as_view())
]
