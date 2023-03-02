# Your Work

Сервис поиска работы и сотрудников

## Стек
- `Django 4.1.7` - основа
- `Django Rest Framework 3.14.0` - для создания REST API на базе Django
- `djangorestframework-simplejwt` - для JWT аутентификации
- `django-cors-headers` - позволяет обращаться к API из других приложений (фронта)
- `drf-yasg` - для автоматической генерации OpenAPI и последующим использовнием в Swager UI
- `pytest` - используется для тестирования (т.к. встроенное Django тестирование не дает удобных и гибких настроек (в частности не позволяет делать фикстуры к тестам))
- `django-debug-toolbar` - позволяет отслеживать запросы к БД и наглядно демонстрирует где их нужно оптимизировать

## Frontend приложение
Имеется простое React JS (с Bootstrap) приложение для этого REST API. 


Для запуска следуйте инструкциям в GitHub репозитории - https://github.com/Protages/your-work-frontend

## Запуск
Клонируем GitHub репозиторий в любую папку
```properties
git clone https://github.com/Protages/your-work-backend
```
Переходим в папку проекта
```properties
cd your-work-backend
```
Создаем виртуальное окружение, активируем его и устанавливаем зависимости (подробнее в requirements.txt)
```properties
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### Создание MVP базы данных
Автоматически создаст тестовую БД (на Windows). После выполнения закройте открывшуюся консоль (если появилась).

**Внимание: Этот скрипт удаляет старую базу данных!**
```properties
.\create_mvp_db.cmd
```
#### Данные для входа как компания
email: `company_1@mail.com`, password: `company1pass`

#### Данные для входа как соискатель
email: `canditate_1@mail.com`, password: `canditate1pass`

#### Данные для входа как суперпользователь
email: `superuser@mail.com`, password: `superuserpass`


При необходимости можно использовать другие данные, смотрите в `src/tests/endpoints/data/` файлы `company_data.py` и `candidate_data.py` соответственно 

### Если не создавали MVP базу данных (выше)
Создаем базу данных в ручную и применяем миграции
```properties
python src/manage.py makemigrations
python src/manage.py migrate
```
---

Запуск приложения локально
```properties
python src/manage.py runserver
```
Теперь REST API доступно по ссылке - http://127.0.0.1:8000/

### Документация
Для удобного ознакомления лучше перейти на http://127.0.0.1:8000/docs/ где распологается Swagger UI, со всеми эндпойнтами и примерами запросов - ответов


## Запуск тестов
Запуск интеграционных тестов
```properties
pytest src/ --verbosity=2 --order-group-scope=module
```

## Прочее
### Использование одной модели User для компании и соискателя
В проекте компания и соискатель привязаны к одной модели User, тем самым упрощается реализация аутентификации для двух (по сути) разных сущностей (не дает существенных нагрузок к БД). Это позволяет использовать встроенные механихме аутентификации Django и (что важнее) иметь уникальное поле для всех клиентов (будь то компания или соискатель - email). При этом один User не может иметь связь с Company (как owner) и с Candidate (как соискатель) одновременно (исключение - User может быть соискателем, и при этом быть сотрудником (не owner) Company (модель Staff (пока не реализовано полноценно))).

### Про выбранную ORM
В качестве ORM выбрана встроенная `Django ORM`, т.к. она не требует дополнительной настройки, проста в использовании и в контексте текущих задач отлично подходит. Встроенные в Django ORM методы select_related и prefetch_related позволяют реализовать достаточно оптимизированные запросы в текущих условиях.

(будь больше времени рассмотрел бы `SQLAlchemy` в Django (уже использовал с FastAPI)).

### Схема базы данных 
Изначально спроектировал схему БД (пока не все реализовано) -
https://drawsql.app/teams/none-831/diagrams/your-work-schema
