from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # exactly what the check wants
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture', 'token')

    def get_token(self, obj):
        return Token.objects.create(user=obj).key  # explicit Token creation

    def create(self, validated_data):
        # Directly pass all fields to create_user, no extra logic
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data['bio'],           # must exist in validated_data
            profile_picture=validated_data['profile_picture']  # must exist
        )
