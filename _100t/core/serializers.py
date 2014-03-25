from rest_framework import serializers
from models import Item, Category, List
from django.contrib.auth.models import User

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('short_name', 'description', 'is_set', 'sub_index')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fileds = ('name', 'owner')

class ItemListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('name', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', )

