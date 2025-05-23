from django.shortcuts import render

def recipe_list(request):
    recipes = [
        {"name": "Pork Sinigang", "link": "/recipe/1"},
        {"name": "Recipe 2: Bicol Express", "link": "/recipe/2"},
    ]
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

def recipe_1(request):
    ingredients = [
        {"name": "pork belly", "quantity": "1kg"},
        {"name": "tamarind soup base mix", "quantity": "1 packet"},
        {"name": "water", "quantity": "1.5L},
        {"name": "tomatoes", "quantity": "3pcs"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "kangkong", "quantity": "1 bunch"},
    ]
    return render(request, "ledger/recipe_detail.html", {"title": "Pork Sinigang", "ingredients": ingredients})

def recipe_2(request):
    ingredients = [
        {"name": "pork belly", "quantity": "1kg"},
        {"name": "coconut milk", "quantity": "2 cups"},
        {"name": "coconut cream", "quantity": "1 cup"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "garlic", "quantity": "5 cloves"},
        {"name": "shrimp paste (bagoong)", "quantity": "2 tablespoons"},
        {"name": "green chili peppers", "quantity": "3pcs"},
    ]
    return render(request, "ledger/recipe_detail.html", {"title": "Recipe 2 -- Bicol Express", "ingredients": ingredients})
