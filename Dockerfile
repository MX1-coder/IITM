FROM python:3


ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

#Directory---
WORKDIR /app

ADD . /app


# COPY ./requirements.txt /app/requirements.txt 

# RUN pip install -r requirements.txt

COPY . /app
CMD ["python", "manage.py","runserver","0.0.0.0.8000",]


# # install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# running migrations
RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py runserver

