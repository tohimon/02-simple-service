FROM python:3.7-slim

COPY . /opt/simple_service

WORKDIR /opt/simple_service

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "simple_service"]
CMD ["1", "2", "3", "4", "5", "6"]