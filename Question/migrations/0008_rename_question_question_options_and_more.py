# Generated by Django 4.2 on 2023-04-12 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0007_remove_question_score_option_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='options',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
    ]