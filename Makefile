COMPOSE = docker-compose -f docker-compose.yml
SERVICE = app

up:
	$(COMPOSE) up

up-d:
	$(COMPOSE) up -d
	
down:
	$(COMPOSE) down

makemigrations:
	$(COMPOSE) run $(SERVICE) alembic revision --autogenerate -m "New Migration"

migrate:
	$(COMPOSE) run $(SERVICE) alembic upgrade head