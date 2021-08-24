from django import template
from django.shortcuts import get_object_or_404

from .models import Follow, Ingredient, Product, Recipe

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


@register.filter(name='extend_context')
def extend_context(context, user):
    context['purchase_list'] = Recipe.objects.filter(purchase_by=user)
    context['favorites'] = Recipe.objects.filter(favorite_by=user)
    return context


@register.filter(name='add_subscription_status')
def add_subscription_status(context, user, author):
    context['is_subscribed'] = Follow.objects.filter(
        user=user, author=author
    ).exists()
    return context