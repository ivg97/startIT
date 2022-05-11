from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerialiser(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email','password',]



