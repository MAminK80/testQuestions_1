# Generated by Django 4.2 on 2023-04-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0024_category_slug_alter_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_list',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
    ]
