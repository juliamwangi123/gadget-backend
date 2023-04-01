from django.urls import path
from gadgethub.views import user_views as views



urlpatterns =[
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
   
    path('register/',views.registerUser,name='register'),
    
    path('profile/',views.getProfile,name='profile'),
    
    path('profile/update/',views.updateProfile,name='update'),
    
    path('info/',views.GetUserProfile,name='infoupdate'),
    
    path('info/update/',views.UpdateUserProfile,name='info'),
    
    
    
    
    
]