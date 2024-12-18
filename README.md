# HOME_WORK_FLASK
Flask API
Инструкция по запуску:

Нужно запустить вертуальное окружение, я использовал PyCharm Professional
Установите в командной строке Flask, если его еще нет: pip install Flask.
Скопируйте файл requirements.txt в папку проекта.
Запустите приложение: python app.py.


Примеры запросов:

Создание поста:
Метод: POST
URL: /posts
Тело: {"title": "Пост", "content": "Текст поста"}

Получение поста:
Метод: GET
URL: /posts/1

Изменение поста:
Метод: PUT
URL: /posts/1
Тело: {"title": "Измененный пост", "content": "Обновленный текст"}

Удаление поста:
Метод: DELETE
URL: /posts/1
