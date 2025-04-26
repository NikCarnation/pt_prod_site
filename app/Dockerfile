FROM python:3.13.2-slim

COPY . /pd_site

WORKDIR /pd_site

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

