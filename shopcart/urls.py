from django.urls import path
from . import views



urlpatterns = [
    path('shopping_carts/', views.ShoppingCartList.as_view()),
    path('shopping_carts/create/', views.ShoppingCartCreate.as_view()),
    path('shopping_carts/<pk>/', views.ShoppingCartRetrieve.as_view()),
    path('shopping_carts/<pk>/update', views.ShoppingCartUpdate.as_view()),
    path('shopping_carts/<pk>/delete', views.ShoppingCartDestroy.as_view()),

    path('api/million/<str:customer_id>/', views.PriceCountAPIView.as_view(), name='price_100_api'),
]