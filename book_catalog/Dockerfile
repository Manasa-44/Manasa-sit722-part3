FROM python:3.11-slim

WORKDIR /app

# Copy the requirements.txt from the book_catalog directory into the container
COPY book_catalog/requirements.txt .

# Copy the app directory from the book_catalog directory into the container's /app directory
COPY book_catalog/app /app

# Install Python dependencies
RUN pip install -r ./requirements.txt

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
