FROM python:3.12-slim
# Set working directory inside the container
WORKDIR /app
# Copy only dependency file first
COPY requirements.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the whole backend code
COPY . .
# Expose backend port
EXPOSE 8000
# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
