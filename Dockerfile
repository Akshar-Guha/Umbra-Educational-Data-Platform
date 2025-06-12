<<<<<<< HEAD
FROM python:3.11.4-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
=======
# Use a lightweight Python base image
FROM python:3.11-slim-buster
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)

# Set the working directory in the container
WORKDIR /app

<<<<<<< HEAD
# Install system dependencies needed for psycopg2 (PostgreSQL client)
# and other potential build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies first
# This allows Docker to cache the layer if requirements.txt doesn't change
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that the application will listen on.
# Render automatically injects the $PORT environment variable.
EXPOSE $PORT

# Command to run the FastAPI application using Uvicorn (used for local testing and potentially for Render direct deploy)
# For Render, the 'startCommand' in render.yaml will override this CMD.
CMD ["uvicorn", "src.api.v1.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Ensure scripts are executable for deployment
RUN chmod +x scripts/*.sh 
=======
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set environment variables for the database connection
# IMPORTANT: For production, use Docker Secrets or Kubernetes Secrets for secure management.
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_NAME=learning_platform_db
ENV DB_USER=learning_user
ENV DB_PASSWORD=1469

# Expose any ports your application might listen on (e.g., if you add a FastAPI app later)
EXPOSE 8000

# Command to run your application (e.g., a simple script, or later your FastAPI app)
CMD ["uvicorn", "src.api.v1.main:app", "--host", "0.0.0.0", "--port", "8000"] 
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
