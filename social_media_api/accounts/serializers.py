from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Explicit CharField for password
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture', 'token')

    def get_token(self, obj):
        # Explicitly create a token
        token = Token.objects.create(user=obj)
        return token.key

    def create(self, validated_data):
        # Use the recommended create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
        )
        return user
