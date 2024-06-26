# Generated by Django 4.1 on 2023-11-16 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recipe_finder_api.Recipe.Model.ModelRecipe


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_api', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cooking_time', models.IntegerField()),
                ('main_picture', models.ImageField(default='not_image.png', upload_to=recipe_finder_api.Recipe.Model.ModelRecipe.namePicture)),
                ('ratings', models.DecimalField(decimal_places=1, default=0.0, max_digits=1, null=True)),
                ('preparation_video', models.CharField(blank=True, max_length=200, null=True)),
                ('is_favorite', models.BooleanField(default=False)),
                ('state', models.SmallIntegerField(default=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(db_column='category_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe_finder_api.category')),
            ],
            options={
                'db_table': 'Recipe',
            },
        ),
        migrations.CreateModel(
            name='Recipe_Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(db_column='ingredient_id', on_delete=django.db.models.deletion.CASCADE, to='recipe_finder_api.ingredient')),
                ('recipe', models.ForeignKey(db_column='recipe_id', on_delete=django.db.models.deletion.CASCADE, to='recipe_finder_api.recipe')),
            ],
            options={
                'db_table': 'Recipe_Ingredient',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(through='recipe_finder_api.Recipe_Ingredient', to='recipe_finder_api.ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
