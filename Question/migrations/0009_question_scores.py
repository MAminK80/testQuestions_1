# Generated by Django 4.2 on 2023-04-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0008_rename_question_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='scores',
            field=models.IntegerField(default=0),
        ),
    ]