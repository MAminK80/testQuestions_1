# Generated by Django 4.2 on 2023-06-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0043_alter_option_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_text', models.CharField(max_length=250)),
                ('second_text', models.CharField(max_length=250)),
                ('third_text', models.CharField(max_length=250)),
                ('fourth_text', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='first_text',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='fourth_text',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='second_text',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='third_text',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
