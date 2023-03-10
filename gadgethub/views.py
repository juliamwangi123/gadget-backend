from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import ProductSerializer,UserSerializer,UserWithRefreshToken
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserWithRefreshToken(self.user).data
        
        for name, value in serializer.items():
            
            data[name] = value
        

       

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    
    serializer_class = MyTokenObtainPairSerializer


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    
    serializer = UserSerializer(user, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    
    product = Product.objects.get(id=pk)
    
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)