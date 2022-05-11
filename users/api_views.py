from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerialiser


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerialiser