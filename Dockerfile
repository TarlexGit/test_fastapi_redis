FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY poetry.lock  pyproject.toml /app/
COPY  backend/app/ /app/
COPY  backend/main.py /app/
RUN pip3 install poetry
RUN poetry install
# CMD ["poetry", "run", "uvicorn", "app.main", "--host", "0.0.0.0", "--port", "80"]
CMD ["poetry", "run", "python", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]