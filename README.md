# FastAPI Template

![FastAPI](https://img.shields.io/badge/FastAPI-v0.103.1-blue?style=flat-square&logo=fastapi)  
Шаблон для создания приложений на основном стеке **FastAPI**, **SQLAlchemy**, **Alembic**, **Pydantic**

---


## 🚀 Запуск
1. Установка Poetry. При проблемах ищите **[решения](https://python-poetry.org/docs/#installing-with-the-official-installer):** 
   
    На `Windows` в PowerShell:

   `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

    На `MacOS/Lunix`

   `curl -sSL https://install.python-poetry.org | python3 -`

2. Добавьте в переменную **PATH**. После установки есть подсказки как это сделать разными способами.

   Например в Windows `C:\Users\<ВашеИмя>\AppData\Roaming\Python\Scripts`

   `Система -> О программе -> Дополнительные параметры системы -> Дополнительно -> Переменные среды -> Path`

3. В терминале ввести `poetry config virtualenvs.in-project true` чтобы .venv окружение создавалось внутри проекта

4. Выполните: `poetry install --no-root` чтобы установить зависимости, указанные в файле pyproject.toml
5. В `PyCharm` откройте `File -> Settings -> Project: <ProjectName> -> Python Interpreter`
6. Нажмите `Add Interpreter` и выберите `Poetry Environment`
7. В разделе `Existing Environment` укажите путь к `python.exe` в папке `.venv` проекта
8. Запустить сервер `uvicorn main:app --reload` из директории `backend`

P.S. Если проект новый и файл pyproject.toml отсутствует, выполните: `poetry init`

## 📋 Описание шаблона

Данный шаблон построен на основе актуальных практик 2024 года и использует **паттерн Repository**

В некоторых файлах можно встретить базовый код (`/backend/core/config.py` к примеру)

### 🛠 Стек технологий:

- **[FastAPI](https://fastapi.tiangolo.com/):** Фреймворк для создания API.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM для работы с базой данных.
- **[Alembic](https://alembic.sqlalchemy.org/):** Инструмент для управления миграциями.
- **[Pydantic](https://docs.pydantic.dev/latest/api/base_model/):** Работа с типами и валидацией данных.
- **[Poetry](https://python-poetry.org/):** Управление зависимостями и виртуальными окружениями.
- **[Docker](https://www.docker.com/):** Контейнеризация приложения.
- **[Redis](https://redis.io/):** Опционально для кэширования.
- **[Ruff](https://docs.astral.sh/ruff/):** Линтер/Форматтер с настройками в pyproject.toml
- **[Black](https://black.readthedocs.io/en/stable/getting_started.html):** Форматтер с настройками в pyproject.toml
- Всё что нужно для работы с PostgreSQL, и aiosqlite (sync/async).
- Библиотеки для тестирования: pyTest, httpx.
- Подробнее в pyproject.toml
---

## 📂 Структура проекта

Шаблон имеет следующую структуру:

```plaintext
fastapi-template/
├── alembic/                  # Каталог миграций Alembic
│   ├── versions/             # Каталог с файлами миграций
│   ├── env.py                # Основной файл конфигурации Alembic
│   └── script.py.mako        # Шаблон для новых миграций
├── backend/
│   ├── __init__.py
│   ├── main.py               # Точка входа FastAPI
│   ├── api/                  # Каталог с API маршрутами
│   ├── core/                 # Конфигурации и основные утилиты
│   ├── models/               # SQLAlchemy модели
│   ├── repositories/         # Репозитории для работы с БД
│   ├── schemas/              # Pydantic схемы
│   ├── services/             # Бизнес-логика
│   └── tests/                # Тесты
├── frontend/                 # По желанию
├── nginx/                    # Под Nginx конфигурацию
├── .env                      # Переменные окружения
├── pyproject.toml            # Poetry конфигурация
├── ruff.toml                 # Ruff конфигурация

