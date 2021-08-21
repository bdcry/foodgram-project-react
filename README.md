После установки docker выполнить команду в командной строке:

    $ docker-compose up

После сборки образа:

    $ sudo docker exec -it <CONTAINER ID> python manage.py collectstatic
    $ sudo docker exec -it <CONTAINER ID> python manage.py makemigrations
    $ sudo docker exec -it <CONTAINER ID> python manage.py migrate
    $ sudo docker exec -it <CONTAINER ID> python manage.py createsuperuser

Выгрузить данные из файла csv:

      $ docker-compose exec -it <CONTAINER ID> python manage.py import_csv


---

я может что-то не так делаю, но у меня все работает при запуске.
if extend_context and add_subscription_status != author


        {% if user.is_authenticated %}
            <button class="button button_style_light-blue" name="purchases" {% if card not in purchase_list %}data-out{% endif %}><span class="{% if card in purchase_list %}icon-check{% else %}icon-plus{% endif %} button__icon"></span>{% if card in purchase_list %}Рецепт добавлен{% else %}Добавить в покупки{% endif %}</button>
            <button class="button button_style_none" name="favorites"{% if card not in favorites %} data-out{% endif %}><span class="icon-favorite{% if card in favorites %} icon-favorite_active{% endif %}"></span></button>
        {% endif %}
    </div>
</div>
