# Generated by Django 2.2 on 2021-08-30 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210830_0046'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='ingredient',
            name='ingredient_unique',
        ),
    ]
