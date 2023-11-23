# Generated by Django 4.1 on 2023-11-23 21:18

from django.db import migrations, models
import django.db.models.deletion
import recipe_finder_api.Recipe.Model.ModelRecipe


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_finder_api', '0007_alter_recipe_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipe', models.ForeignKey(db_column='recipe_id', on_delete=django.db.models.deletion.CASCADE, related_name='step', to='recipe_finder_api.recipe')),
            ],
            options={
                'db_table': 'Step',
            },
        ),
        migrations.CreateModel(
            name='StepAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('step', models.ForeignKey(db_column='step_id', on_delete=django.db.models.deletion.CASCADE, to='recipe_finder_api.step')),
            ],
            options={
                'db_table': 'StepAction',
            },
        ),
        migrations.CreateModel(
            name='ExtraImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to=recipe_finder_api.Recipe.Model.ModelRecipe.nameExtraPicture)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_pictures', to='recipe_finder_api.recipe')),
            ],
        ),
    ]
