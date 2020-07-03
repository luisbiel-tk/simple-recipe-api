from django.db import models


class RecipeManager(models.Manager):
    def create_recipe(self, recipe: dict, ingredients: list):
        recipe = Recipe.objects.create(**recipe)
        recipe.add_ingredients(ingredients=ingredients)

        return recipe


class Recipe(models.Model):
    objects = RecipeManager()

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)

    def add_ingredients(self, ingredients):
        for ingredient in ingredients:
            Ingredient.objects.create(recipe=self, **ingredient)

    def update_ingredients(self, ingredients):
        Ingredient.objects.filter(recipe=self).delete()
        self.add_ingredients(ingredients)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')