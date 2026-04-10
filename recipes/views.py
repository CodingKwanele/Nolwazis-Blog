from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe
from .forms import RecipeForm


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')

    difficulty = request.GET.get('difficulty', '').strip()
    if difficulty in ('easy', 'medium', 'hard'):
        recipes = recipes.filter(difficulty=difficulty)

    paginator = Paginator(recipes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'recipes': page_obj,
        'page_obj': page_obj,
        'selected_difficulty': difficulty,
    }
    return render(request, 'recipes/recipe_list.html', context)


@login_required
def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients_list = [ing.strip() for ing in recipe.ingredients.split(',')] if recipe.ingredients else []

    instructions_steps = []
    for i, step in enumerate(recipe.instructions.strip().split('\n'), 1):
        step = step.strip()
        if step:
            instructions_steps.append((i, step))

    context = {
        'recipe': recipe,
        'ingredients_list': ingredients_list,
        'instructions_steps': instructions_steps,
    }
    return render(request, 'recipes/recipe_detail.html', context)


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Share Your Recipe'})


@login_required
def recipe_update(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Edit Recipe'})


@login_required
def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


@login_required
def recipe_search(request):
    query = request.GET.get('q', '').strip()
    recipes = Recipe.objects.filter(title__icontains=query).order_by('-created_at') if query else Recipe.objects.none()
    return render(request, 'recipes/recipe_search.html', {'recipes': recipes, 'query': query})


def register(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = UserCreationForm()
    # Add Bootstrap styling to all fields
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control form-control-lg'})
    return render(request, 'recipes/register.html', {'form': form})
