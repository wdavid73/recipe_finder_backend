# Generated by Django 4.1 on 2023-11-23 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_api', '0007_alter_recipe_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionPicturesRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipe', models.ForeignKey(db_column='recipe_id', on_delete=django.db.models.deletion.CASCADE, to='recipe_finder_api.recipe')),
            ],
            options={
                'db_table': 'OptionPicturesRecipe',
            },
        ),
    ]