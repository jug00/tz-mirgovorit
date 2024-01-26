from django.urls import path
from .views import add_product_to_recipe, cook_recipe, show_recipes_without_product


urlpatterns = [
    path(
        "add-product/<int:recipe_id>/<int:product_id>/<int:weight>/",
        add_product_to_recipe,
        name="add_product_to_recipe",
    ),
    path("cook-recipe/<int:recipe_id>/", cook_recipe, name="cook_recipe"),
    path(
        "show-recipes/<int:product_id>/",
        show_recipes_without_product,
        name="show_recipes_without_product",
    ),
]
