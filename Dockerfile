# Use a base Python image
FROM python:3.12.0-slim

# Define the working directory
WORKDIR /

# Copy the requirements file and install dependencies
RUN mkdir -p /app
COPY ./app/requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application files
COPY ./app /app

# Expose the port that Gunicorn will use
EXPOSE 5000

# Command to start the application
CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "app.wsgi:app"]
