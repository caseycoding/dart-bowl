# START some general stuff that is nice to develop with

#REGISTRY_URL=aws ecr url

# aws-login:
# 	aws ecr get-login --no-include-email --region us-west-2 | sh

# END

build-backend-docker-container:
	docker build --rm -t bowling-backend -f ./backend/.docker/Dockerfile ./backend

mount-backend-docker-container:
	docker run --rm -ti -p 5000:5000 -v `pwd`/backend:/code -w /code bowling-backend:latest bash

up-fullstack:
	docker-compose -f .docker-compose/fullstack.yml up

down-fullstack:
	docker-compose -f .docker-compose/fullstack.yml down

test-backend:
	docker run --rm -ti -v `pwd`/backend:/code -w /code bowling-backend:latest pytest