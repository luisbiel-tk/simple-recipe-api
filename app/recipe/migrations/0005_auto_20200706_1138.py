# Generated by Django 3.0.8 on 2020-07-06 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipe.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.TextField(),
        ),
    ]