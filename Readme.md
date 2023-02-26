# Your Work

Сервис поиска работы и сотрудников

## Стек
- `Django 4.1.7` - основа
- `Django Rest Framework 3.14.0` - для создания REST API
- `djangorestframework-simplejwt` - для JWT аутентификации
- `django-cors-headers` - позволяет обращаться к API из других приложений (фронта)
- `drf-yasg` - для автоматической генерации Swager UI
- `pytest` - используется для тестирования (т.к. встроенное Django тестирование не дает удобных гибких настроек)
- `django-debug-toolbar` - позволяет отслеживать запросы к БД

## Запуск
Клонируем GitHub репозиторий
```properties
git clone https://github.com/Protages/your-work-backend
```
Создаем виртуальное окружение, активируем и устанавливаем зависимости
```properties
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### Создание MVP базы данных
Автоматически создаст тестовую БД (на Windows). После выполнения закройте открывшуюся консоль.
#### Внимание: Удаляет старую базу данных!
```properties
.\create_mvp_db.cmd
```
#### Данные для входа как компания
email: `company_1@mail.com`, password: `company1pass`

#### Данные для входа как соискатель
email: `canditate_1@mail.com`, password: `canditate1pass`

### Если не создавали MVP базу данных
Создаем базу данных в ручную и применяем миграции
```properties
python src/manage.py makemigrations
python src/manage.py migrate
```
---

Запускаем API
```properties
python src/manage.py runserver
```

### Документация
Для удобного ознакомления лучше перейти на http://127.0.0.1:8000/docs/ где распологается Swagger UI


## Запуск тестов
Запуск интеграционных тестов
```properties
pytest --verbosity=2 --order-group-scope=module
```

## Прочее
### Про выбранную ORM
В качестве ORM выбрана встроенная `Django ORM`, т.к. не требует отдельной настройки и проста в использовании (будь больше времени рассмотрел бы `SQLAlchemy`).

### Схема базы данных 
https://drawsql.app/teams/none-831/diagrams/your-work-schema
