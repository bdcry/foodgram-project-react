from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название тега')
    slug = models.SlugField(unique=True, verbose_name='Slug тега')

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Теги'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(
        max_length=100, verbose_name='Название ингредиента')
    unit = models.CharField(max_length=10, verbose_name='Единица измерения')

    class Meta:
        verbose_name_plural = 'Ингредиенты'
        verbose_name = 'Ингредиенты'

    def __str__(self):
        return f'{self.title}, {self.unit}'


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower',
                             verbose_name='Пользователь подписчик')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='following',
                               verbose_name='Пользователь на которого подписываемся')

    class Meta:
        db_table = 'posts_follow'
        verbose_name_plural = 'Подписки'
        verbose_name = 'Подписки'
        constraints = [models.UniqueConstraint(fields=['user', 'author'],
                                               name='follow_unique')]

    def __str__(self):
        return f'{self.author}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='recipes')
    title = models.CharField(verbose_name='Название рецепта', max_length=50)
    image = models.ImageField(
        verbose_name='Фото блюда', upload_to='recipes/', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    ingredients = models.ManyToManyField(Product, through='Ingredient',
                                         related_name='recipes', blank=True,
                                         verbose_name='Ингредиенты рецепта')
    tags = models.ManyToManyField(
        Tag, verbose_name='Тэги', blank=True, related_name='recipes')
    time = models.PositiveIntegerField(verbose_name='Время приготовления')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True)
    favorite_by = models.ManyToManyField(User, through='Favourite',
                                         related_name='favorite_recipes',
                                         blank=True,
                                         verbose_name='Избранный рецепт')
    purchase_by = models.ManyToManyField(User, through='ShopList',
                                         related_name='shop_list',
                                         blank=True,
                                         verbose_name='Список покупок')

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Рецепты'
        verbose_name = 'Рецепты'

    def __str__(self):
        return f'{self.title}'


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Ингредиент в рецепте')
    ingredient = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Рецепт')
    amount = models.PositiveIntegerField(verbose_name='Количество ингредиента')

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукты'
        constraints = [models.UniqueConstraint(
            fields=['ingredient', 'amount', 'recipe'],
            name='ingredient_unique')]

    def __str__(self):
        return f'{self.amount}'


class Favourite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    created = models.DateTimeField(
        verbose_name='Дата добавления', auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Избранное'
        verbose_name = 'Избранное'
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe', 'created'],
            name='favourite_unique')]

    def __str__(self):
        return f'{self.recipe}'


class ShopList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    created = models.DateTimeField(
        verbose_name='Дата добавления', auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Список покупок'
        verbose_name = 'Список покупок'
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe', 'created'],
            name='shoplist_unique')]

    def __str__(self):
        return f'{self.recipe}'
