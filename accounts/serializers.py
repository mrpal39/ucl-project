from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers
from .models import User


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token["username"] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name',
        'password', 'password2',]
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }

        def save(self):
                user = User(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                )

                password = self.validated_data['password']
                password2 = self.validated_data['password2']

                if password != password2:
                    raise serializers.ValidationError({'password':'Passwords must match.'})
                user.set_password(password)
                user.save()
                return user