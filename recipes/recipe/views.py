from django.shortcuts import render, redirect

from recipes.recipe.forms import CreateRecipeForm, DeleteRecipeForm
from recipes.recipe.models import Recipe


def home(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request, "index.html", context)


def create_recipe(request):
    if request.method == "POST":
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = CreateRecipeForm()
    context = {
        "form": form,
    }
    return render(request, "create.html", context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = CreateRecipeForm(instance=recipe)
    context = {
        "form": form,
        "recipe": recipe,
    }
    return render(request, "edit.html", context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("home")

    form = DeleteRecipeForm(instance=recipe)
    context = {
        "form": form,
        "recipe": recipe,
    }
    return render(request, "delete.html", context)


def show_recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    separated_ingredients = recipe.ingredients.split(", ")
    context = {
        "recipe": recipe,
        "separated_ingredients": separated_ingredients,
    }
    return render(request, "details.html", context)
