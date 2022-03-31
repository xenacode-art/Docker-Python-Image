FROM python 

WORKDIR /app

COPY . /app

CMD ["python", "Auto-Mail-Deletion.py"]
