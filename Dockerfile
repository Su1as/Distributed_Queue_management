# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Install system dependencies for Flask-Migrate
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN python -m pip install mysqlclient==1.4.2.post1

ENV FLASK_APP=server.py
# Run Flask-Migrate to handle database migrations
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run server.py when the container launches
CMD ["python", "server.py"]
