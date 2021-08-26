После установки docker выполнить команду в командной строке:

    $ docker-compose up

После сборки образа:

    $ sudo docker exec -it <CONTAINER ID> python manage.py collectstatic
    $ sudo docker exec -it <CONTAINER ID> python manage.py makemigrations
    $ sudo docker exec -it <CONTAINER ID> python manage.py migrate
    $ sudo docker exec -it <CONTAINER ID> python manage.py createsuperuser

Выгрузить данные из файла csv:

      $ docker-compose exec -it <CONTAINER ID> python manage.py import_csv

IP: http://130.193.41.213
админка: Tim pw: 0906