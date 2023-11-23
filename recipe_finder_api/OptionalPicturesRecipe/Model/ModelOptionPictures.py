from datetime import date
from django.db import models
from recipe_finder_api.Recipe.Model.ModelRecipe import Recipe

def namePicture(instance, filename):
    todays_date = date.today()
    return "/".join(["images", "recipes", "{}".format(todays_date.year), filename])

class OptionPicturesRecipe(models.Model):
    picture = models.ImageField(
        upload_to=namePicture, default='not_image.png', null=False)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, db_column="recipe_id", null=False
    )
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "OptionPicturesRecipe model"

    class Meta:
        db_table = "OptionPicturesRecipe"
