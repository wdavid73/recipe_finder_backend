from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from recipe_finder_api.Category.Model.ModelCategory import Category
from recipe_finder_api.Ingredient.Model.ModelIngredient import Ingredient
from recipe_finder_api.models import CustomUser


def namePicture(instance, filename):
    todays_date = date.today()
    return "/".join(["images", "recipes", "{}".format(todays_date.year), filename])


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cooking_time = models.IntegerField(blank=False, null=False)
    main_picture = models.ImageField(
        upload_to=namePicture, default='not_image.png', null=False)
    ratings = models.DecimalField(null=True, blank=False, default=0.0, decimal_places=1, max_digits=2, validators=[
                                  MinValueValidator(0.0), MaxValueValidator(5.0)])
    preparation_video = models.CharField(max_length=200, blank=True, null=True)
    is_favorite = models.BooleanField(default=False, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, db_column="category_id", null=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, db_column='user_id', null=True)
    ingredient = models.ManyToManyField(
        Ingredient, through="Recipe_Ingredient")
    ###
    state = models.SmallIntegerField(default=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, \nCategory: {},\nUser: {}".format(self.name, self.category, self.user)

    class Meta:
        db_table = "Recipe"


class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, db_column="recipe_id")
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Recipe_Ingredient"


"""
? STATES
* 0 -> disable
* 1 -> visible / enable
* 2 -> hide
* 3 -> draw

? IS_FAVORITE
* false -> is no favorite
* true -> is favorite
"""
