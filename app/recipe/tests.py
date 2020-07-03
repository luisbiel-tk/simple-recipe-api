import uuid
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Recipe, Ingredient
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

    def test_get_recipe_detail_with_ingredients(self):
        recipe = Recipe.objects.create(name='Gambas al ajillo', description='Gambas con ajo, aceite y perejil')
        Ingredient.objects.create(name='Gambas', recipe_id=recipe.id)
        Ingredient.objects.create(name='Ajo', recipe_id=recipe.id)
        Ingredient.objects.create(name='Aceite', recipe_id=recipe.id)

        serialized_recipe = RecipeSerializer(recipe)
        response = self.client.get(recipe_detail_url(recipe.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_recipe.data)

    def test_get_recipe_detail_returns_not_found(self):
        res = self.client.get(recipe_detail_url(1234))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_recipe_with_ingredients(self):
        ingredientName1 = "Pelota"
        ingredientName2 = "Caldo"
        payload = {
            "name": "Escudella",
            "description": "Nunca he sabido hacerlo... pero la de Iaia esta bien buena",
            "ingredients": [{"name": ingredientName1}, {"name": ingredientName2}]
        }

        response = self.client.post(RECIPE_URL, payload, format='json')
        recipe = Recipe.objects.get(id=response.data['id'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #Checking everything but the ingredients
        for key in payload.keys():
            if key != 'ingredients':
                self.assertEqual(payload[key], getattr(recipe, key))
        #Checking ingredients
        self.assertTrue(recipe.ingredients.get(name=ingredientName1))
        self.assertTrue(recipe.ingredients.get(name=ingredientName2))
