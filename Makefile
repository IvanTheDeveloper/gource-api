up-dev:
	docker compose -f docker-compose.dev.yml up --build

#	For port mapping to work, either set the CONTAINER_PORT env var to the desired container port,
#	either use parameter --env-file .env to set the CONTAINER_PORT env var from a .env file.
#	Container port in the -p param of the docker run command MUST ALWAYS match the port specified through
#	params. If params are not set, port must match the Dockerfile EXPOSE instruction port (8080 by default).
#	Using param --rm is usually not needed in production.
up-prod:
	docker build -t my-app:latest . && \
	docker run --rm -p 8080:8443 -e CONTAINER_PORT=8443 my-app:latest
