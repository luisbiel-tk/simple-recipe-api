from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Recipe
from .serializers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')

def recipe_detail_url(recipe_id):
    return reverse('recipe:recipe-detail', args=[recipe_id])


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

    def test_get_recipe_detail(self):
        recipe = Recipe.objects.create(name='Caracoles', description='Caracoles a la llauna o con sofrito')
        res = self.client.get(recipe_detail_url(recipe.id))
        serialized_recipe = RecipeSerializer(recipe)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serialized_recipe.data)

    def test_get_recipe_detail_returns_not_found(self):
        res = self.client.get(recipe_detail_url(1234))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)