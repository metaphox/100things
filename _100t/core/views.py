from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Item, Category, List, Enlist
from serializers import ItemSerializer, CategorySerializer, ItemListSerializer, UserSerializer, EnlistSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = List.objects.all()
    serializer_class = ItemListSerializer

class EnlistViewSet(viewsets.ModelViewSet):
    queryset = Enlist.objects.all()
    serializer_class = EnlistSerializer

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def itemlist_list(request, format=None):
    if request.method == 'GET':
        lists = List.objects.all()
        serializer = ItemListSerializer(lists, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def itemlist_detail(request, pk, format=None):
    return Response(status=status.HTTP_204_NO_CONTENT)
