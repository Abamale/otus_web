# OTUS Capstone Project

## Тема

**Development of Automated API and UI Tests with Selenium, Pytest, and Allure Reporting for Remote Execution**

---

## Описание

В данном репозитории представлены автоматизированные тесты, разработанные в рамках итогового проекта на курсе OTUS.

### Реализованные тесты:

1. **API-тест** для сервиса [reqres.in/api](https://reqres.in)
2. **UI-тесты** для платформы [OpenCart](https://demo.opencart.com)

Результаты выполнения тестов оформлены в виде **Allure-отчёта**.  
Сборка и запуск тестов осуществляется через **Jenkins**, работающий в Docker-контейнере.

---

## Используемые технологии

- **Selenium** – автоматизация UI-тестов  
- **Pytest** – основной фреймворк для тестирования  
- **Allure** – генерация отчётов о запуске тестов  
- **Requests** – выполнение API-запросов  
- **Faker** – генерация тестовых данных  
- **Pydantic** – валидация JSON-схем  
- **Logger** – логирование  
- **Jenkins** – CI/CD и удалённый запуск  
- **Docker** – контейнеризация и локальный запуск сервисов

---

## Структура проекта

```
.
├── tests/
│   ├── test_api/               # API-тесты
│   └── test_ui/                # UI-тесты
├── utils/
│   ├── data_generator.py       # Генерация данных через Faker
│   └── schemas/                # Pydantic-схемы для API-валидации
├── docker-compose.yml          # Запуск OpenCart
├── Dockerfile                  # Сборка Jenkins
└── reports/
    └── allure-results/         # Результаты тестов для Allure
```

---

## Детали запуска

### Jenkins

- Jenkins собирается из `Dockerfile`
- Доступен по порту **8085**

Запуск Jenkins:
```bash
docker build -t jenkins-capstone -f Dockerfile .
docker run -p 8085:8080 jenkins-capstone
```

### OpenCart

- Запускается через `docker-compose.yml`
- Доступен по адресу: [http://localhost:8081](http://localhost:8081)

Команда запуска:
```bash
docker-compose up -d
```

---

## Allure-отчёт

После выполнения тестов для просмотра отчёта используйте команду:
```bash
allure serve reports/allure-results
```

Откроется локальный сервер с визуализацией результатов в браузере.

---

## Дополнительно

- **Валидация JSON-ответов** реализована с помощью **Pydantic-моделей**, расположенных в `utils/schemas/`
- **Генерация тестовых данных** для UI-тестов выполняется через библиотеку **Faker**, см. `utils/data_generator.py`

---

## Автор Марина Абакумова

Итоговый проект по курсу «Python QA Engineer» на платформе OTUS  