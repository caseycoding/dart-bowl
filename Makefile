# START some general stuff that is nice to develop with

#REGISTRY_URL=aws ecr url

# aws-login:
# 	aws ecr get-login --no-include-email --region us-west-2 | sh

# END

build-flask-docker-container:
	docker build --rm -t bowling-backend -f ./backend/.docker/Dockerfile ./backend/.docker

mount-backend-docker-container:
	docker run --rm -ti -p 5000:5000 -v `pwd`/backend:/code -w /code bowling-backend:latest bash

up-dev:
	docker-compose -f .docker-compose/fullstack.yml up

down-dev:
	docker-compose -f .docker-compose/fullstack.yml down
