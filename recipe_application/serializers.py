from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_ingredients(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Ingredients must be a list")
        return value

    def validate_instructions(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Instructions must be a list")
        return value