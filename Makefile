up:
	docker-compose up --build

down:
	docker-compose down --remove-orphans

migrations:
	docker-compose run server python manage.py makemigrations \
		&& docker-compose run server python manage.py migrate

migrate:
	docker-compose run server python manage.py migrate

connect:
	docker-compose run server bash

api_schema:
	docker-compose run server python manage.py \
		spectacular --force-color --fail-on-warn --format openapi 1> etc/api-schema.yaml 2> tmp/cmd.err ; \
		cat tmp/cmd.err \

manage:
	docker-compose run server python manage.py

