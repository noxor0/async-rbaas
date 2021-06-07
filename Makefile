.PHONY: help

install:  ## Install requirements for entire app
	virtualenv venv
	source venv/bin/activate && pip install -e .[dev]

up: ## Start Django app
	source venv/bin/activate && python manage.py runserver

run: ## Run the warrior app against a Django server
	source venv/bin/activate && python warrior/main.py 'boss/1' 'boss/2' 'boss/3'

populate_db: ## Populate db with some test data for tests
	source venv/bin/activate && python manage.py migrate
	source venv/bin/activate && python scripts/populate_db.py

drop_db: ## "Drop" the db
	rm -f db.sqlite3

test: ## Integration test for warrior app
	source venv/bin/activate && cd warrior && python -m pytest


help: ## Print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
