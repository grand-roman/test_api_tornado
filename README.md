

## Задание: 
Реализовать CRUD сервис, который обрабатывает, принимает и
хранит тела запросов, а также считает количество одинаковых запросов. Тела запросов хранятся по ключу (строка).
Ключ генерируется из параметров тела запроса, методом “ключ+значение”, после чего кодируется в base64.

## Запросы
### /api/duplicate
Получение процента дубликатов от общего количества запросов
В случае отсутствия дубликатов возвращаем уведомление об их отсутствии

### /
Получение полного списка запросов

### /api
#### GET 
Получения запроса по ключу
#### POST
Создание тела запроса и генерация ключа POST
#### DELETE
Удаление запроса по ключу
#### DELETE
Изменение тела запроса и создание нового ключа, счетчик дубликатов обнуляется 


## Требования к технологиям:
1. Веб-фреймворк–TornadoWebFramework;
2. СервисработаетпоархитектурномустилюREST;
3. Приложение должно заворачиваться в docker контейнер. И предоставлять
docker-compose.yml для автоматического развертывания на localhost-е приложение должно в одну команду: “docker-compose up”