from django.urls import path
from . import views 



urlpatterns = [

    path('items/', views.ItemListView.as_view()),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/update/', views.ItemUpdateView.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),

    path('api/customer/<str:user_id>/purchases/', views.UserPurchasesView.as_view()),
]