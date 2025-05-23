from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RecipeForm, RecipeIngredientFormSet, RecipeImageForm

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

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            formset.instance = recipe
            formset.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet()
    return render(request, 'ledger/recipe_add.html', {'form': form, 'formset': formset})


@login_required
def add_recipe_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = RecipeImageForm()
    return render(request, 'ledger/image_upload.html', {'form': form, 'recipe': recipe})


