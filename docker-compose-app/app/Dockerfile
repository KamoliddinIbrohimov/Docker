FROM python:alpine

WORKDIR /app

RUN  pip install --upgrade pip\
     pip install pymongo

COPY . .

CMD [ "python", "main.py" ]