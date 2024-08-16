# Документация по запуску проекта

## Требования

- Python 3.x
- PostgreSQL
- Git
- Virtualenv (или любой другой инструмент для создания виртуальных окружений)

## Шаги по запуску проекта

### 1. Клонирование репозитория

### Сначала клонируйте репозиторий с проектом:

```bash
git clone https://github.com/Vento741/Dj_diplom_Social_Network.git
cd spd-diplom\social_network
```


### 2. Создание виртуального окружения

Создайте виртуальное окружение для проекта:

```bash
python -m venv env
```

Активируйте виртуальное окружение:

- **Для Windows:**

  ```bash
  .\env\Scripts\activate
  ```

- **Для macOS/Linux:**

  ```bash
  source env/bin/activate
  ```

### 3. Установка зависимостей

Установите все необходимые зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных

1. Убедитесь, что PostgreSQL установлен и запущен.
2. Создайте базу данных для проекта.:

   ```sql
   CREATE DATABASE dj_diplom;
   ```

3. Настройте параметры подключения к базе данных в файле `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'dj_diplom',
           'USER': 'ваш_пользователь',
           'PASSWORD': 'ваш_пароль',
       }
   }
   ```

### 5. Миграции базы данных

Примените миграции для создания таблиц в базе данных:

```bash
python manage.py migrate
```

### 6. Создание суперпользователя

Создайте суперпользователя для доступа к административной панели:

```bash
python manage.py createsuperuser
```

Следуйте инструкциям на экране для ввода данных суперпользователя.

### 7. Запуск сервера разработки

Запустите сервер разработки Django:

```bash
python manage.py runserver
```

Сервер будет доступен по адресу `http://127.0.0.1:8000/`.

### 8. Доступ к API

Используйте Postman для взаимодействия с API. Не забудьте добавлять токен авторизации в заголовки запросов.

### 9. Административная панель

Перейдите по адресу `http://127.0.0.1:8000/admin/` для доступа к административной панели. Войдите с использованием данных суперпользователя, созданного ранее.

## Дополнительные настройки

### Настройка `MEDIA` и `STATIC` файлов

Добавьте следующие настройки в `settings.py`:

```python
# Медиа файлы (загружаемые пользователем)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## Примеры запросов в Postman

```bash
Создание поста

URL: http://127.0.0.1:8000/api/posts/
Method: POST
Authorization: Bearer Token
Body: form-data
text (string)
image (file)
```

```bash
Получение постов

URL: http://127.0.0.1:8000/api/posts/
Method: GET
Authorization: Bearer Token
```
```bash
Добавление комментария

URL: http://127.0.0.1:8000/api/posts/{post_id}/comments/
Method: POST
Authorization: Bearer Token
Body: raw JSON
text (string)
```
```bash
Постановка лайка

URL: http://127.0.0.1:8000/api/posts/{post_id}/likes/
Method: POST
Authorization: Bearer Token
```

## Создание поста с геоданными:

### Отправьте POST-запрос на /api/posts/ с полями text, location_name и при необходимости images.

Пример тела запроса:

```python
{
  "text": "Посещение нового места",
  "location_name": "Эйфелева башня, Париж",
  "images": [1, 2]  // ID изображений, если применимо
}
```
