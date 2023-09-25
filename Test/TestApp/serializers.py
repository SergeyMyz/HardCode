from rest_framework import serializers
from .models import Product, Lesson, User, View


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = "__all__"
