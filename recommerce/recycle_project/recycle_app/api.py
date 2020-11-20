from django.contrib.auth.models import User
from rest_framework import viewsets,permissions
from recycle_app.serializer import UserSerializer

class ViewSet(viewsets.ModelViewSet):
    users=User.objects.all()
    serializer_class = UserSerializer
