from django.urls import path
from . import views

urlpatterns = [

    path('customers/', views.CustomerList.as_view()),
    path('customers/create/', views.CustomerCreate.as_view()),
    path('customers/<pk>/', views.CustomerRetrieve.as_view()),
    path('customers/<pk>/update', views.CustomerUpdate.as_view()),
    path('customers/<pk>/delete', views.CustomerDestroy.as_view()),
]