# Проект Sports Tourism

## О проекте

Этот проект представляет собой REST API для спортивного туризма, реализованный с использованием FastAPI и SQLAlchemy. Он позволяет управлять данными о турах, туристах, маршрутах и других сущностях, связанных со спортивным туризмом.

## Установка и запуск проекта

### Предварительные требования

- Python 3.8 или выше
- PostgreSQL (или другая поддерживаемая база данных)

### Установка

```bash
   git clone https://github.com/yourusername/sports_tourism.git
   cd sports_tourism
 # Получение всех туров
GET /tours/

# Ответ
[
    {
        "id": 1,
        "name": "Горный поход на Эльбрус",
        "description": "Недельный поход на самую высокую вершину Европы.",
        "duration_days": 7
    },
    ...
]
# Создание нового тура
POST /tours/
{
    "name": "Поход по Карпатам",
    "description": "Двухнедельный поход по Карпатам.",
    "duration_days": 14
}
# Ответ
{
    "id": 2,
    "name": "Поход по Карпатам",
    "description": "Двухнедельный поход по Карпатам.",
    "duration_days": 14
}
