from django.urls import path
from . import views



urlpatterns =[
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('',views.apiRoutes,name='apiRoutes'),
    path('products/',views.getProducts,name='products'),
    path('products/<int:pk>/',views.getProduct,name='product'),
    path('user/profile/',views.getProfile,name='profile'),
    
    
    
    
]