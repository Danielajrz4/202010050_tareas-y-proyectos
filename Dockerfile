FROM python:3.9

WORKDIR /home/daniela/Desktop/app

COPY . .

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y postgresql-client \
    && apt-get clean

RUN pip install -r requirements.txt

ENV DATABASE_URL=postgres://postgres:PutaMadre123$@dbultima.cjae6om8gxml.us-east-2.rds.amazonaws.com:5432/ultima

COPY . .

EXPOSE 8000

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]