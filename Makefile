.PHONY: help build up down restart logs

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

restart: down up

logs:
	docker-compose logs -f

helm-install:
	helm install note-app ./helm/note_app

helm-upgrade:
	helm upgrade note-app ./helm/note_app

helm-uninstall:
	helm uninstall note-app
