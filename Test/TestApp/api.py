from .models import Product, Lesson, User, View
from rest_framework import viewsets, permissions
from .serializers import ViewSerializer, ProductSerializer


class ViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ViewSerializer


class LessonsSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer
