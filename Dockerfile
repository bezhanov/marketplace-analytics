FROM python:3.12

WORKDIR /code

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /code/

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./app /code/app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]