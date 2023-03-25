
from rest_framework.decorators import api_view,permission_classes,APIView
from rest_framework.response import Response
from gadgethub.serializers import UserSerializer,UserWithRefreshToken,UserProfileSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from gadgethub.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserWithRefreshToken(self.user).data
        
        for name, value in serializer.items():
            
            data[name] = value
        

       

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    fullname = data['name']
    
    try:
        
        
        first_name, last_name = fullname.split()
    
    except:
        message ={ "detail": "Fullname must include first and last name separated by a space"}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.create(
            first_name= first_name,
            last_name= last_name,
            username=data['email'],
            email =data['email'],
            password = make_password(data['password'])
        ) 
        serializer = UserWithRefreshToken(user, many=False)
        return Response(serializer.data)
    except:
        message = { "detail":"Email already exists"}
        
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    
    serializer = UserSerializer(user, many=False)
    
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user=request.user
    
    serializer = UserSerializer(user, many=False)
    
    data = request.data
    
    # user.first_name = data["name"]
    user.last_name = data["lastname"]
    user.username = data["email"]
    
    user.first_name = data["firstname"]
    user.email = data["email"]
    
    if data["password"] != "":
        user.password = make_password(data['password'])
    
    
    user.save()
    
    return Response(serializer.data)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserProfile(request):
    try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            serializer = UserProfileSerializer(user_profile,many=False)

            return Response(serializer.data,status=status.HTTP_200_OK)
    except:
        return Response(
            {'error': 'Something went wrong when retrieving profile'},
            status= status.HTTP_404_NOT_FOUND
        )


@api_view(['PUT'])
@permission_classes([IsAuthenticated])   
def UpdateUserProfile(request):
    user = request.user
    data = request.data
    user_profile = UserProfile.objects.get(user=user)
    
    user_profile.address = data["address"]
    user_profile.city = data["city"]
    user_profile.country = data["country"]
    user_profile.gender = data["gender"]
    user_profile.phone = data["phone"]
    
   
    user_profile.save()
    
    serializer = UserProfileSerializer(user_profile,many=False)
    
    
    return Response(serializer.data)
          