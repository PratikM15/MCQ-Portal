# Generated by Django 3.1.6 on 2021-06-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
