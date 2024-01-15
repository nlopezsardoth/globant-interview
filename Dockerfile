FROM python:3-alpine3.18

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]