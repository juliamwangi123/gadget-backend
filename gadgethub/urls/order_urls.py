from django.urls import path
from gadgethub.views import order_views as views



urlpatterns =[
   
    
    path('add/order/',views.addOrderItems,name='addorder'),
    path('myorders/',views.getUserOrders,name='myoders'),
    path('<str:pk>/',views.getOrder,name='userorder'),
    path('<str:pk>/pay/',views.orderPayment,name='paid'),

    
]