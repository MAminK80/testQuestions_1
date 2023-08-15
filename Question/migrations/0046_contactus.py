# Generated by Django 4.2 on 2023-08-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0045_questionnaire_category_questionnaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=700)),
            ],
        ),
    ]
