FROM --platform=linux/amd64 python:3.10-slim
 
WORKDIR /app
 
COPY requirements.txt .
 
RUN pip install -r requirements.txt
 
COPY . .
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7001"]


