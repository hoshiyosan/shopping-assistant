
serve:
	cd shopping_assistant \
		&& ../.venv/bin/uvicorn shopping_assistant:api --host 0.0.0.0 --reload


container:
	docker build -t backend .
	docker run -p 5000:80 backend
