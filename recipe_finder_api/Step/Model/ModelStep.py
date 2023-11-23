from django.db import models
from recipe_finder_api.Recipe.Model.ModelRecipe import Recipe


class Step(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    recipe = models.ForeignKey(
        Recipe,
        related_name='step',
        on_delete=models.CASCADE,
        db_column="recipe_id",
        null=False
    )
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Step"
        ordering = ['created_at']

class StepAction(models.Model):
    action = models.CharField(max_length=150, null=False, blank=False)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, db_column='step_id', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "{}, {}".format(self.action, self.step)
    
    class Meta:
        db_table = "StepAction"
        ordering = ['created_at']