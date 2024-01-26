from django.db import models


# Класс Product представляет продукты, которые могут быть использованы в рецептах
# Поле name хранит название продукта, а uses_count хранит количество использований продукта.
class Product(models.Model):
    name = models.CharField(max_length=255)
    uses_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Класс Recipe представляет рецепты блюд
# Поле name хранит название рецепта, а поле products хранит список продуктов, входящих в рецепт
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through="RecipeProduct")

    # Метод add_product добавляет продукт в рецепт или если он уже есть в рецепте, то заменяет вес в рецепте
    def add_product(self, product_id, weight):
        product = self.recipeproduct_set.get(product_id=product_id)
        if product:
            product.weight = weight
            product.save()
        else:
            RecipeProduct.objects.create(recipe=self, product=product_id, weight=weight)

    # Метод inc_recipe_count увеличивает количество использований каждого из продуктов в рецепте
    def inc_recipe_count(self):
        objs = []
        for product in self.products.all():
            obj = product
            obj.uses_count += 1
            objs.append(obj)
        self.products.bulk_update(objs, ["uses_count"])

    def __str__(self):
        return self.name


# Класс RecipeProduct представляет связь между продуктом и рецептом
# Поле product хранит ссылку на продукт, а поле recipe хранит ссылку на рецепт
class RecipeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.IntegerField()
