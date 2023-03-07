from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def apiRoutes(request):
    endpoints=[
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/',
        '/api/products/top/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]
    
    return JsonResponse(endpoints,safe=False)