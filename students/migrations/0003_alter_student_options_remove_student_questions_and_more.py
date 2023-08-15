# Generated by Django 4.2 on 2023-04-13 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0010_remove_question_options_remove_question_scores_and_more'),
        ('students', '0002_student_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='options',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question.option'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='questions',
        ),
        migrations.AddField(
            model_name='student',
            name='questions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Question.question'),
            preserve_default=False,
        ),
    ]