from django import template
from django.shortcuts import get_object_or_404

from .models import Ingredient, Product

register = template.Library()


def tag_filter(model, tags):
    if tags:
        return model.objects.prefetch_related(
            'author', 'tags'
        ).filter(
            tags__slug__in=tags
        ).distinct()
    else:
        return model.objects.prefetch_related(
            'author', 'tags'
        ).all()


def get_ingredients_from_form(ingredients, recipe):
    ingredients_for_save = []
    for ingredient in ingredients:
        product = get_object_or_404(Product, title=ingredient['title'])
        ingredients_for_save.append(
            Ingredient(recipe=recipe, ingredient=product,
                       amount=ingredient['amount']))
    return ingredients_for_save
