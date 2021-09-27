from rest_framework.viewsets import ModelViewSet

from authapp.models import UserProfile
from authapp.serializers import UserProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
