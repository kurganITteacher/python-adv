from rest_framework.serializers import ModelSerializer

from authapp.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'gender', 'date_birth')
