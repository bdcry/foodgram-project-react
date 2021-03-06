# Generated by Django 2.2 on 2021-08-30 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='amount',
            name='recipe',
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('ingredient', 'amount', 'recipe'), name='ingredient_unique'),
        ),
        migrations.DeleteModel(
            name='Amount',
        ),
    ]
