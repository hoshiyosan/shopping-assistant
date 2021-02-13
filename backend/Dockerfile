FROM python:3.7

WORKDIR /app
COPY shopping_assistant/ /app/shopping_assistant

RUN pip install shopping_assistant/

EXPOSE 80

CMD ["uvicorn", "shopping_assistant:api", "--host", "0.0.0.0", "--port", "80"]
