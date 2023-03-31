
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from gadgethub.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status
from gadgethub.models import *
from rest_framework.views import APIView
from django.core.files.base import ContentFile
from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Q
from django.utils import timezone



@api_view(['GET'])
def getProducts(request):
  
    query = request.query_params.get("search")
    if query == None:
        query = ""
    
    
    products = Product.objects.filter(title__icontains=query).order_by('-createdAt').all()
    
    page = request.query_params.get("page")
    # products = Product.objects.order_by('-createdAt').all()
    paginator = Paginator(products,6)
    
    try:
        products = paginator.page(page)
        
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        products = paginator.page(paginator.num_pages)
    
    if page == None:
        page = 1
    
    page = int(page)
                    
    # products = Product.objects.filter(
    #             Q(description__icontains=searc) | Q(name__icontains=search)
    #         )
   
    
    serializer = ProductSerializer(products, many=True)
    
    return Response({"products": serializer.data, "page":page,"pages":paginator.num_pages})

@api_view(['GET'])
def getProduct(request,pk):
    
    product = Product.objects.get(id=pk)
    
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)



class createProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    # user= request.user
    # data = request.data
    # def base64_to_image(base64_string):
    #     format, imgstr = base64_string.split(';base64,')
    #     ext = format.split('/')[-1]
    #     return ContentFile(base64.b64decode(imgstr), name=uuid.uuid4().hex + "." + ext)
    
    # image = base64_to_image(data["image"])
    # product = Product.objects.create(
    #     user=user,
    #     title= data["title"],
    #     image= image,
    #     description=data["description"],
    #     paymentMethod=data["paymentMethod"],
    #     bank = data["bank"],
    #     accName=data["accName"],
    #     accNumber = data["accNumber"],
    #     condition = data["condition"],
    #     currency = data["currency"],
    #     itemVisibility = data["itemVisibility"],
    #     price = data["price"],
        
    # )
    
    # serializer = ProductSerializer(data,many=False)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SoldProductsView(APIView):
    def get(self, request):
        sold_products = Product.objects.filter(isSold=True, user=request.user)
        serializer = ProductSerializer(sold_products, many=True)
        return Response(serializer.data)
    
class SavedProductsView(APIView):
    def get(self, request):
        saved_products = Product.objects.filter(isSaved=True, user=request.user)
        serializer = ProductSerializer(saved_products, many=True)
        return Response(serializer.data)
    
    
    
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])   
def saveItem(request,pk):
    
    product = Product.objects.get(id=pk)
 
    product.isSaved = True
    
  
   
    product.save()
    
    return Response({"detail": "Product saved successful"})
    
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def getUserProducts(request):
    
    user = request.user
    products = user.product_set.all()
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])   
def deleteItem(request,pk):
    user = request.user
    product = Product.objects.get(id=pk,user=user)
 
    product.delete()
    
  
   
    
    return Response({"detail": "Product deleted successful"})