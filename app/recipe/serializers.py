from rest_framework.serializers import ModelSerializer
from .models import Recipe, Ingredient

RECIPE_INGREDIENTS = 'ingredients'

class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class RecipeSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', RECIPE_INGREDIENTS, 'created_at')
        read_only_views = ('id',)

    def create(self, validated_data):
        ingredients = validated_data.pop(RECIPE_INGREDIENTS, None)
        recipe = Recipe.objects.create_recipe(recipe=validated_data, ingredients=ingredients)

        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.get(RECIPE_INGREDIENTS)
        if ingredients:
            instance.update_ingredients(ingredients=ingredients)

        return instance



