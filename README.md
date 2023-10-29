#### Тестовое задание компании ItFactory

### Clone:
    git clone -b review https://github.com/Flashvita/it-factory.git

### Run with docker compose:
    .env поместить в рабочую директорию(где manage.py, пример example.env)
    docker compose up --build
    docker compose -it <container_id> bash
    python manage.py createsuperuser


### Админ панель:
    http://0.0.0.0:8080/admin
    
### Документация:
    http://0.0.0.0:8080/api/schema/swagger-ui/



