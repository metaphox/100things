from rest_framework import serializers
from models import Item, Category, List
from django.contrib.auth.models import User

class EnlistSerializer(serializers.Serializer):
    pk = serializers.Field()
    item_list = serializers.Field()
    item = serializers.Field()

class ItemHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'short_name', 'description', 'is_set', 'sub_index')

class ItemSerializer(serializers.Serializer):
    pk = serializers.Field()

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fileds = ('id', 'name', 'owner')

class ItemListHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'title', 'owner', 'items')

class ItemListSerializer(serializers.Serializer):
    pk = serializers.Field()
    title = serializers.CharField(max_length=50)
    owner = serializers.Field()
    created = serializers.Field()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', )

