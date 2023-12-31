FROM python:3
ENV PYTHONBUFFERED=1

ENV PYTHONBUFFERED=1
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip \ 
    && pip install -r requirements.txt

COPY . /app
EXPOSE 8000

COPY ./contrib/docker/setup.sh /setup.sh
RUN chmod +x /setup.sh

CMD ["/setup.sh"]