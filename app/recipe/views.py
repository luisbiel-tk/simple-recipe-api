from rest_framework import viewsets, mixins

from .models import Recipe
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer