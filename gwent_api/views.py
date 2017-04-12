from rest_framework.decorators import api_view
from .models import Card, Category, Faction, Group, Rarity
from .serializers import (
    CardSerializer, CardListSerializer, CategorySerializer,
    FactionSerializer, GroupSerializer, RaritySerializer
    )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import json
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cards': reverse('card-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'factions': reverse('faction-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'rarities': reverse('rarity-list', request=request, format=format),
    })


class RarityList(APIView):
    
    def get(self, request, format = None):
        rarities = Rarity.objects.all()
        serializer = RaritySerializer(rarities,  context={'request': request}, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = RaritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FactionList(APIView):
    
    def get(self, request, format = None):
        factions = Faction.objects.all()
        serializer = FactionSerializer(factions,  context={'request': request}, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = FactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupList(APIView):
    def get(self, request, format = None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups,  context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryList(APIView):
    
    def get(self, request, format = None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,  context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardList(APIView):
    """
    List all Cards, or create a new card.
    """

    def get(self, request, format=None):
        cards = Card.objects.all()
        # print cards
        serializer = CardListSerializer(cards, context={'request': request}, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardDetail(APIView):
    """
    Retrieve, update or delete a card instance.
    """

    def get_object(self, pk):
        try:
            return Card.objects.get(pk=pk)
            
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)


'''
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
