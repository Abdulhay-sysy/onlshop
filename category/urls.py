from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/create/', views.CategoryCreate.as_view()),
    path('categories/<pk>/', views.CategoryRetrieve.as_view()),
    path('categories/<pk>/update', views.CategoryUpdate.as_view()),
    path('categories/<pk>/delete', views.CategoryDestroy.as_view()),
]