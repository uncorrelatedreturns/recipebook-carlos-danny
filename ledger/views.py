from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})


def recipe_1(request):
    context = {
        "title": "Pork Sinigang",
        "ingredients": [
            {"name": "pork belly", "quantity": "1kg"},
            {"name": "tamarind soup base mix", "quantity": "1 packet"},
            {"name": "water", "quantity": "1.5L"},
            {"name": "tomatoes", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "kangkong", "quantity": "1 bunch"},
            {"name": "sitaw (string beans)", "quantity": "1 cup"},
        ]
    }
    return render(request, "ledger/recipe_detail.html", context)

def recipe_2(request):
    context = {
        "title": "Bicol Express",
        "ingredients": [
            {"name": "pork belly", "quantity": "1kg"},
            {"name": "coconut milk", "quantity": "2 cups"},
            {"name": "coconut cream", "quantity": "1 cup"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "garlic", "quantity": "5 cloves"},
            {"name": "shrimp paste (bagoong)", "quantity": "2 tablespoons"},
            {"name": "green chili peppers", "quantity": "3pcs"},
        ]
    }
    return render(request, "ledger/recipe_detail.html", context)
