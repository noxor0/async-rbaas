.PHONY: help

install:
	pip ins

populate_db:
	python scripts/populate_db.py

test: ## Integration test for warrior script
	cd warrior && python -m pytest
	cd ..


help: ## Print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
