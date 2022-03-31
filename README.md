После установки docker выполнить команду в командной строке:

    $ docker-compose up

После сборки образа:

    $ docker-compose exec web python manage.py migrate
    $ docker-compose exec web python manage.py loaddata tags.json
    $ docker-compose exec web python manage.py collectstatic
    $ docker-compose exec web python manage.py createsuperuser

Выгрузить данные из файла csv:

      $ docker-compose exec web python manage.py import_csv
