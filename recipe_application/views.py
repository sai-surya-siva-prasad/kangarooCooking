from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = Recipe.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            recipes = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query)
            ).distinct()[:5]  # Limit to 5 results
            serializer = self.get_serializer(recipes, many=True)
            return Response(serializer.data)
        return Response([])

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()