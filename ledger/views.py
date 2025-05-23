from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})
# Example access using hint: Ingredient.objects.filter(recipe__recipe__name="<Name of Recipe>")

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipe_list')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'ledger/login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')



