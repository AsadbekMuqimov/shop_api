from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, register, login_view

urlpatterns = [
    path('product/list/', ProductList.as_view(), name='product-list'),  
    path('product/detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),  
    

    path('category/list/', CategoryList.as_view(), name='category-list'),  
    path('category/detail/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),  


    path('register/', register, name='register'), 
    path('login/', login_view, name='login'),  
]