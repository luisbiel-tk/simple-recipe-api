from rest_framework.serializers import ModelSerializer
from .models import Recipe, Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class RecipeSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', 'ingredients', 'created_at')
        read_only_views = ('id',)

    def create(self, validated_data):
        ingredients = validated_data.get('ingredients')
        del validated_data['ingredients']
        recipe = Recipe.objects.create_recipe(recipe=validated_data, ingredients=ingredients)

        return recipe


