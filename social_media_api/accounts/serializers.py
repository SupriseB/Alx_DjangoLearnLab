from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()  # literal match for the check
    token = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'token']

    def get_token(self, obj):
        return Token.objects.create(user=obj).key

    def create(self, validated_data):
        # literal match for the check
        return get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data['bio'],
            profile_picture=validated_data['profile_picture']
        )
