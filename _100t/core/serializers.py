from rest_framework import serializers
from models import Item, Category, List
from django.contrib.auth.models import User

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('item_list', 'index', 'is_set', 'sub_index', 'short_name', 'description')

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

