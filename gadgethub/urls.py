from django.urls import path
from . import views

urlpatterns =[
    
    path('',views.apiRoutes,name='apiRoutes')
]