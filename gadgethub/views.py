from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

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