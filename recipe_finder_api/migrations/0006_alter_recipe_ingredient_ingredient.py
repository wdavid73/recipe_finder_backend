# Generated by Django 4.1 on 2023-11-16 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_api', '0005_recipe_recipe_ingredient_recipe_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_ingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_finder_api.ingredient'),
        ),
    ]
