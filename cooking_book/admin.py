from django.contrib import admin

from .models import Recipe, Product, RecipeProduct


# Класс RecipeProductAdmin наследуется от admin.StackedInline и используется для
# отображения информации о связи между рецептами и продуктами в административном интерфейсе.
class RecipeProductAdmin(admin.StackedInline):
    model = RecipeProduct


# Класс RecipeAdmin наследуется от admin.ModelAdmin и используется для настройки
# отображения информации о рецептах в административном интерфейсе.
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductAdmin]
    list_display = ("name", "id")

    class Meta:
        model = Recipe


# Класс ProductAdmin используется для настройки отображения информации
# о продуктах в административном интерфейсе.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

    class Meta:
        model = Product


# Регистрация моделей Recipe и Product в административном интерфейсе
# с использованием соответствующих классов администратора.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Product, ProductAdmin)
