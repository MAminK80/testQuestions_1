# Generated by Django 4.2 on 2023-04-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0012_remove_option_question_option_question'),
        ('students', '0003_alter_student_options_remove_student_questions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='options',
        ),
        migrations.AddField(
            model_name='student',
            name='options',
            field=models.ManyToManyField(to='Question.option'),
        ),
    ]
