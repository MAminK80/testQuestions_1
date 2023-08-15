# Generated by Django 4.2 on 2023-04-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0020_alter_question_answer_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]