FROM python
LABEL mantainer="sergioarroyopay@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

EXPOSE 8000

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
