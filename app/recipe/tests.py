from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Recipe
from .serializers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')


class RecipeApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_all_recipes(self):

        Recipe.objects.create(name='Tortilla', description='Tortilla de patatas con cebolla')
        Recipe.objects.create(name='Banderilla', description='Pincho de olivas y boquerones')

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        res = self.client.get(RECIPE_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(len(res.data), len(serializer.data))
