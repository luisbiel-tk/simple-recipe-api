from rest_framework import viewsets, mixins

from .models import Recipe
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = self.queryset

        searchText = self.request.query_params.get('name')
        if searchText:
            queryset = queryset.filter(name__contains=searchText)

        return queryset