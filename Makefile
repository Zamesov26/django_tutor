.PHONY: lint

# Линтинг и автоформатирование кода
lint:
	ruff format .
	ruff check . --select I --fix
	ruff check . --fix