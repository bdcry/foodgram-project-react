# Generated by Django 2.2 on 2021-08-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20210830_0047'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('ingredient', 'amount', 'recipe'), name='ingredient_unique'),
        ),
    ]
