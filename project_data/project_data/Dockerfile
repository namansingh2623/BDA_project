# Start from official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy all project files (adjust this if your folder structure is different)
COPY . /app

# Install system-level dependencies (if needed, like gcc for building packages)
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# (Create a requirements.txt with your dependencies OR list them here)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the Dash app port (change if your app runs on another port)
EXPOSE 8050

# Command to run the Dash app
CMD ["python", "apps.py"]