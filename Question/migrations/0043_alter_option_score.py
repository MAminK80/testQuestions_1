# Generated by Django 4.2 on 2023-06-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0042_remove_question_answer_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]