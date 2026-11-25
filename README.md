# Учебный проект: Git и Docker

**Студент:** Кузьменко Валентин Сергеевич  
**Группа:** БИ-3-24-02

## О проекте
Небольшое Python-приложение демонстрирует базовую работу с исходным кодом, историей Git и контейнеризацией Docker. Приложение выводит приветствие и сведения о проекте.

## Требования
- Git
- Python 3.11+ (для запуска без Docker)
- Docker с поддержкой Compose (для контейнерного запуска)

## Запуск без Docker
```bash
python3 src/main.py
```

## Запуск в Docker
Сборка и запуск:
```bash
docker compose up --build
```
Остановка:
```bash
docker compose down
```

## Структура
```text
git-docker-practice/
├── .github/
│   ├── workflows/ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── src/main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── compose.yaml
└── README.md
```

## Проверка
```bash
python3 src/main.py
docker compose config
docker build -t git-docker-practice .
docker run --rm git-docker-practice
```

## Практика Git
Выполнены локальные операции: инициализация репозитория, коммиты, просмотр истории и различий, создание ветки и слияние. Публикация в GitHub, Pull Request в веб-интерфейсе, приглашение пользователя и настройка правил защиты требуют действий в личном аккаунте GitHub. Пошаговая инструкция приведена в `../ОТЧЕТ_ПРАКТИКА_GIT.docx` и `GITHUB_CHECKLIST.md`.

## Автор
Кузьменко Валентин Сергеевич, БИ-3-24-02.

## Pull Request check
This change demonstrates a feature branch, pull request, and code review.
