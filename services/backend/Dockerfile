FROM python:3.8-slim 

WORKDIR /services/backend

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

EXPOSE 3000

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh


