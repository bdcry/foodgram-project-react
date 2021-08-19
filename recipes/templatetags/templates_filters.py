from django import template

from recipes.models import Follow, Recipe

register = template.Library()


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
    