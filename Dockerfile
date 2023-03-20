# BUILDER
FROM python:3.10.5-slim as builder

WORKDIR /core/app/src

# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install gcc python3-dev musl-dev postgresql postgresql-contrib

RUN pip install --upgrade pip
COPY ./requirements/base.txt .
COPY ./requirements/development.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /core/app/src/wheels -r development.txt

COPY ./src .


# FINAL #
FROM python:3.10.5-slim

# Create directory for the app user
RUN mkdir -p /home/app

# Create group - app, user - app
RUN addgroup --system app && adduser --system app && adduser app app

# Create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install dependencies
RUN apt-get update
COPY --from=builder /core/app/src/wheels /wheels
COPY --from=builder /core/app/src/development.txt .
RUN pip install --no-cache /wheels/*

# Copy project
COPY . $APP_HOME

# Chown all the files to the app user
RUN chown -R app:app $APP_HOME

# Change to the app user
USER app
