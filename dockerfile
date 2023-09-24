FROM python:3.11
#RUN useradd -m -s /bin/bash guest_user
#USER guest_user
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/