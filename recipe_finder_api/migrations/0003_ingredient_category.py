# Generated by Django 4.1 on 2023-11-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_api', '0002_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Dairy', 'Dairy'), ('Seasoning', 'Seasoning'), ('Oil', 'Oil'), ('Vegetable', 'Vegetable'), ('Grain', 'Grain'), ('Protein', 'Protein'), ('Fruit', 'Fruit'), ('Sweetener', 'Sweetener'), ('Seasoning', 'Seasoning'), ('Dried fruit', 'Dried fruit'), ('Dessert', 'Dessert'), ('Herb', 'Herb')], default='Basic', max_length=100),
        ),
    ]