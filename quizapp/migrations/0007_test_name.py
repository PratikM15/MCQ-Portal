# Generated by Django 3.2.7 on 2021-09-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0006_remove_question_is_compulsory'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
