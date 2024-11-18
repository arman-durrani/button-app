#base image
FROM python:3.8.20

#set work directory
WORKDIR /home/button-app

#stop buffer
ENV PYTHONUNBUFFERED=1

#install dependencies
RUN pip install --upgrade pip
RUN pip install django

#copy whole project to your docker home directory
COPY . .

#port where the Django app runs
EXPOSE 8000

#start server
CMD python manage.py runserver 0.0.0.0:8000