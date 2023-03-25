from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.utils import timezone

from gadgethub.serializers import ProductSerializer,OrderSerializer

from rest_framework import status
from gadgethub.models import Product, Order,OrderItem,ShippingAddress
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    
    orderItems = data['orderItems']
    
    if orderItems and len(orderItems) == 0:
        
        return Response({'detail':"No order Items"},status=status.HTTP_400_BAD_REQUEST)
    
    else:
        order = Order.objects.create(
            user=user,
            orderNumber = data["orderNumber"],
            paymentMethod=data["paymentMethod"],
            totalPrice=data["totalPrice"]
        )
        
        shipping = ShippingAddress.objects.create(
            order= order,
            address = data["shippingDetails"]["address"],
            city=data["shippingDetails"]["city"],
            country= data["shippingDetails"]["country"]
        )
        
        for i in orderItems:
            product = Product.objects.get(id=i['id'])
            
            first_dict = product.uploaded_images.first()
            
            item = OrderItem.objects.create(
                product=product,
                order=order,
                name = product.title,
                price = product.price,
                image = first_dict.image
                
            )
    serializer = OrderSerializer(order,many=False)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrder(request,pk):
    user = request.user
    
    order = Order.objects.get(id=pk)
    
    try:
        if user.is_staff or order.user == user:
            
            serializer = OrderSerializer(order, many=False)
            
            return Response(serializer.data)
        
        else:
            
            return Response({"detail": "Authentication credentials were not provided."}, status= status.HTTP_401_UNAUTHORIZED)
    
    
    except:
        
        return Response({"detail":"Order does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def getUserOrders(request):
    
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    
    return Response(serializer.data)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])   
def orderPayment(request,pk):
    
    order = Order.objects.get(id=pk)
  
    order.isPaid = True
    order.paidAt = timezone.now()
    order.save()
    
    return Response({"detail": "Order payment successful"})
    