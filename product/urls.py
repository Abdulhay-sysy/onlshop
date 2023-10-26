from . import views
from django.urls import path

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/create/', views.ProductCreate.as_view()),
    path('products/<pk>/', views.ProductRetrive.as_view()),
    path('products/<pk>/update', views.ProductUpdate.as_view()),
    path('products/<pk>/delete', views.ProductDestroy.as_view()),

    path('most-sold-product/', views.MostSoldProductView.as_view(), name='most-sold-product'),
    path('total_inentory_price/', views.TotalInventoryPrice.as_view(), name='total_inentory_price'),
    path('Expired/', views.ExpiredProducts.as_view(), name='Expired'),
]