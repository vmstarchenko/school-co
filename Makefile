up:
	docker-compose up --build

down:
	docker-compose down --remove-orphans

migrations:
	docker-compose run server python manage.py makemigrations \
		&& docker-compose run server python manage.py migrate

migrate:
	docker-compose run server python manage.py migrate

createsuperuser:
	docker-compose run server python manage.py createsuperuser

connect:
	docker-compose run server bash

api_schema:
	docker-compose run server python manage.py \
		spectacular --force-color --fail-on-warn --format openapi 1> ./etc/api-schema.yaml 2> tmp/cmd.err ; \
		cat tmp/cmd.err \

api_client: api_schema
	rm -rf ./var/volumes/api_client/* && \
	cp etc/api-schema.yaml etc/docker/openapitools/api-schema.yaml && \
	docker build etc/docker/openapitools -t local-openapitools && \
	docker run -v "${PWD}/var/volumes/api_client":/home/user/api_client --rm local-openapitools \
		generate -i ./etc/api-schema.yaml -g typescript-angular -o ./api_client/ts_angular && \
	docker run -v "${PWD}/var/volumes/api_client":/home/user/api_client --rm local-openapitools \
		generate -i ./etc/api-schema.yaml -g python -o ./api_client/py && \
	rm -r ./ui/src/api.d ; \
	cp -r ./var/volumes/api_client/ts_angular ./ui/src/api.d

manage:
	docker-compose run server python manage.py


