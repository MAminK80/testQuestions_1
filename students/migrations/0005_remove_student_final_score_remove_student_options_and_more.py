# Generated by Django 4.2 on 2023-04-18 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0015_remove_question_options_option_question'),
        ('students', '0004_remove_student_options_student_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='final_score',
        ),
        migrations.RemoveField(
            model_name='student',
            name='options',
        ),
        migrations.AddField(
            model_name='student',
            name='options',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Question.option'),
            preserve_default=False,
        ),
    ]