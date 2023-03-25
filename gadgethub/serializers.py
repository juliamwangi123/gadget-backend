from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product,Order,OrderItem,ShippingAddress,ItemImages,UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__' 
        
        
class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    firstname = serializers.SerializerMethodField(read_only=True)
    lastname = serializers.SerializerMethodField(read_only=True)
    isSeller = serializers.SerializerMethodField(read_only=True)
    
    
    
    class Meta:
        model = User
        fields = ['id','username','email','name','isSeller','firstname','lastname']
        
    def get_name(self,obj):
        name = obj.first_name
        
        if name == "":
            name = obj.email
        
        return name
    
    def get_firstname(self,obj):
        firstname = obj.first_name
        
        return firstname
    
    
    
    
    
    def get_lastname(self,obj):
        lastname = obj.last_name
        if lastname == "":
            lastname = obj.first_name
        
        return lastname
    
    def get_isSeller(self,obj):
        
        return obj.is_staff
    
    
class UserWithRefreshToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','email','name','isSeller','token','firstname','lastname']
          
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
    
   
    
    

    

class ItemImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImages
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    uploaded_images = ItemImagesSerializer(many=True)
    user = UserSerializer(read_only=True)
    
    
    # uploaded_images = serializers.ListField(
    #     child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = True),
    #     write_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ["id","description","paymentMethod","bank","currency","accName","accNumber","condition","itemVisibility","price","images","uploaded_images"]

    def create(self,validated_data):
        images = validated_data.pop('uploaded_images')
        
        product_instance = Product.objects.create(**validated_data)
        for image in images:
            newP = ItemImages.objects.create(product=product_instance,**image)
        return product_instance
    
    def get_user(self,request):
        
        user = request.user
        serializer = UserSerializer(user,many=False)  
        return serializer.data
    # def create(self, validated_data):
    #     uploaded_images = validated_data.pop("uploaded_images")
    #     product = Product.objects.create(**validated_data)
    #     for image in uploaded_images:
    #         newproduct = ItemImages.objects.create(product=product, image=image)
            
    #     return product    
        
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
        
        
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        
        
        
class OrderSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model = Order
        fields = '__all__'
        
        
    def get_orders(self,obj):
        
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items,many=True)  
        return serializer.data 
    
    
    def get_shippingAddress(self,obj):
        try:
            address = ShippingAddressSerializer(obj.shippingaddress,many=False)
            
        except:
            address =False
            
        return address.data
    
    
    def get_user(self,obj):
        
        user = obj.user
        serializer = UserSerializer(user,many=False)  
        return serializer.data
        