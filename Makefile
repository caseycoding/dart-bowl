# START some general stuff that is nice to develop with

#REGISTRY_URL=aws ecr url

# aws-login:
# 	aws ecr get-login --no-include-email --region us-west-2 | sh

# END

# needed to build the docker container, typically folled by a push to ecr
build-backend-docker-container:
	docker build --rm -t bowling-backend -f ./backend/.docker/Dockerfile ./backend

# can be used to just mount the backend container =
mount-backend-docker-container:
	docker run --rm -ti -p 5000:5000 -v `pwd`/backend:/code -w /code bowling-backend:latest bash

# can be used to mount into the container for testing, need a better way to do this
mount-fullstack:
	BACKEND_ENTRYPOINT='bash' docker-compose -f .docker-compose/fullstack.yml up

mount-into-fullstack:
	docker exec -it bowling-backend /bin/bash

up-fullstack:
	BACKEND_ENTRYPOINT='bash start.sh' docker-compose -f .docker-compose/fullstack.yml up

down-fullstack:
	docker-compose -f .docker-compose/fullstack.yml down
