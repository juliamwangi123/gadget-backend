from django.urls import path
from . import views

urlpatterns =[
    
    path('',views.apiRoutes,name='apiRoutes'),
    path('products/',views.getProducts,name='products'),
    path('products/<int:pk>/',views.getProduct,name='product')
    
    
]