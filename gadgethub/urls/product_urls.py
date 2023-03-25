from django.urls import path,include
from gadgethub.views import product_views as views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("newItem", views.createProduct)
urlpatterns =[
   
    path('',views.getProducts,name='products'),
    path('<int:pk>/',views.getProduct,name='product'),
    path('', include(router.urls)),
     
    
]