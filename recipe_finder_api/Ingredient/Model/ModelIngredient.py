from django.db import models
from django.urls import reverse

categories = [
    ('Basic', 'Basic'),
    ('Dairy', 'Dairy'),
    ('Seasoning', 'Seasoning'),
    ('Oil', 'Oil'),
    ('Vegetable', 'Vegetable'),
    ('Grain', 'Grain'),
    ('Protein', 'Protein'),
    ('Fruit', 'Fruit'),
    ('Sweetener', 'Sweetener'),
    ('Seasoning', 'Seasoning'),
    ('Dried fruit', 'Dried fruit'),
    ('Dessert', 'Dessert'),
    ('Herb', 'Herb'),
]


class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=100, blank=False, null=False, choices=categories, default='Basic')
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.category)

    class Meta:
        db_table = "Ingredient"