# Generated by Django 4.2 on 2023-04-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0019_question_answer_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_score',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='selected_answer',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
    ]