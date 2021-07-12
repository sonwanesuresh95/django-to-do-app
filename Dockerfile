FROM python:3.6-slim
RUN mkdir /Django_app
WORKDIR /Django_app
ADD . /Django_app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
