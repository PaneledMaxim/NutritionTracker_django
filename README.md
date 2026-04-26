# Nutrition Tracker

Учебный Django-проект для учета питания, продуктов, рецептов и социальной активности пользователей.

## Стек

- Python 3.9+
- Django 4.2
- SQLite


## Запуск проекта

```bash
python manage.py migrate
python manage.py runserver
```

## Распределение по веткам

- `main` или `master` — общий стабильный код
- `feature/users` — регистрация, логин, профиль, друзья (Гуртов)
- `feature/diary` — продукты, дневник питания, калории (Петриков)
- `feature/recipes` — рецепты, ингредиенты, API (Седых)



