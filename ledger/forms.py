from django import forms
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage
from django.forms import inlineformset_factory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

RecipeIngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, fields=('ingredient', 'quantity'), extra=2)

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']