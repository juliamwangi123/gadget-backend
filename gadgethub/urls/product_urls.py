from django.urls import path,include
from gadgethub.views import product_views as views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("newItem", views.createProduct)
urlpatterns =[
   
    path('',views.getProducts,name='products'),
    path('sold/items/', views.SoldProductsView.as_view(), name='sold_products'),
    path('saved/items/', views.SavedProductsView.as_view(), name='saved_products'),
    path('myitems/', views.getUserProducts, name='user_products'),
    path('delete/<int:pk>/', views.deleteItem, name='delete_products'),
    
    path('<int:pk>/',views.getProduct,name='product'),
    path('', include(router.urls)),
     
    
]