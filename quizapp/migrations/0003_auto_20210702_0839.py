# Generated by Django 3.1.6 on 2021-07-02 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_test_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_organizer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='compulsary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.test'),
        ),
    ]
