from python:3.8.10
RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./library/ ./
#COPY ./DRF/ ./
RUN pip3 install -r requirements.txt
#RUN python3 -m pip install -r requirements.txt

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

FROM nginx:1.19.6-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d



