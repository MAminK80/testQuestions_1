# Generated by Django 4.2 on 2023-04-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0018_question_selected_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
