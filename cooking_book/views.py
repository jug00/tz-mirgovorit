from django.shortcuts import render
from django.http import HttpResponse

from cooking_book.models import Recipe, Product, RecipeProduct


# Функция add_product_to_recipe принимает id рецепта, id продукта и вес продукта в граммах
# Она добавляет продукт в рецепт и возвращает статус 200 в случае успеха
def add_product_to_recipe(request, recipe_id, product_id, weight):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.add_product(product_id, weight)
    except (Recipe.DoesNotExist, RecipeProduct.DoesNotExist):
        return HttpResponse(status=404)
    return HttpResponse(status=200)


# Функция cook_recipe принимает id рецепта и увеличивает количество использований продуктов в рецепте
# Она возвращает статус 200 в случае успеха
def cook_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return HttpResponse(status=404)
    recipe.inc_recipe_count()
    return HttpResponse(status=200)


# Функция show_recipes_without_product принимает id продукта и возвращает список рецептов,
# в которых указанный продукт отсутствует или присутствует в количестве меньше 10 грамм
def show_recipes_without_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    q1 = Recipe.objects.filter(
        recipeproduct__product=product, recipeproduct__weight__lt=10
    )
    q2 = Recipe.objects.exclude(recipeproduct__product=product)
    recipes = q1.union(q2)
    return render(
        request, "recipes_table.html", context={"recipes": recipes, "product": product}
    )
