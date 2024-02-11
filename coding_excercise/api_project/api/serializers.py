# api/serializers.py

from rest_framework import serializers
from .models import Company, Client, ClientUser

# api/serializers.py

from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Enter a valid email address',
        ),
    ])

    class Meta:
        model = User
        fields = '__all__'

# Define other serializers with regex validation as required


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = '__all__'

# Define other serializers as required
