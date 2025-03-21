FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 9567
CMD ["uvicorn", "frontend:app", "--host", "0.0.0.0", "--port", "9567"]
