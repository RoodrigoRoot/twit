run:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose -f docker-compose.yml stop

bash:
	docker-compose -f docker-compose.yml exec backend sh

migrations:
	docker-compose -f docker-compose.yml exec backend ./manage.py makemigrations

migrate:
	docker-compose -f docker-compose.yml exec backend ./manage.py migrate

logs:
	docker-compose -f docker-compose.yml logs -f backend