# Generated by Django 3.0.8 on 2020-07-02 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='created',
            new_name='created_at',
        ),
    ]
