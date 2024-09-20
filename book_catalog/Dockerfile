FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
COPY ./app .
RUN pip install -r ./requirements.txt

# Install Python dependencies
RUN pip install -r ./requirements.txt

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
