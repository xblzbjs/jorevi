SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: ## Poetry install
	poetry install

.PHONY: check
check: ## Run check
	poetry run python manage.py check

.PHONY: check-deploy
check-deploy: ## Run check in prod
	poetry run python manage.py check --deploy

.PHONY: test
test: ## Run tests
	poetry run pytest .

.PHONY: run
run: ## Run the Django server
	poetry run python manage.py runserver

clean_migration_files: ## Clean all migration files
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

clean_db: ## Run reset_db in dev
	poetry run python manage.py reset_db --noinput

migration: ## Make and run migrations
	poetry run python manage.py makemigrations

migrate: ## Make and run migrate
	poetry run python manage.py migrate

requirements: ## Generate dev and prod requirements
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	poetry export --without-hashes --dev --format=requirements.txt > requirements-dev.txt

fake_blog: ## Generate fake blog data
	poetry run python manage.py fake_blog

fake_company: ## Generate fake company data
	poetry run python manage.py fake_company 50

start: install check migration migrate run ## Install requirements, apply migrations, then start development server
