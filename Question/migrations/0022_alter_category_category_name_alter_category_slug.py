# Generated by Django 4.2 on 2023-04-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0021_category_slug_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
