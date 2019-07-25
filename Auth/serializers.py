from rest_framework import serializers
from rest_framework import  exceptions
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username','')
        password = data.get('password','')

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User is deactive"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login"
                raise exceptions.AuthenticationFailed(msg)    
        else:
            msg = "Please provide username and password"
            raise exceptions.ValidationError(msg)
        return data

    """
     Register User  

    """
class RegisterUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
            max_length=100,
            required = True,
            validators = [UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
            max_length=100,
            required = True,
            validators = [UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
            max_length=15,
            required = True,
            min_length=8, 
            write_only=True
        )
    first_name = serializers.CharField(
            max_length=100,
            required = True
        )
    last_name = serializers.CharField(
            max_length=100,
            required = True
        )
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],            
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user 

    class Meta:
        model = User
        fields = ('id','username','password','email','first_name','last_name')
        validators = ()


                    