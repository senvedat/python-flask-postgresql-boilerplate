# Start from golang base image
FROM python:3.10-alpine

# Working directory
WORKDIR /app

# Copy requirments files
COPY requirements.txt ./

# Install requirments
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy everythings
COPY . .

# Expose port 8080 to the outside world
EXPOSE 5000

# Envs included
ENV PYTHONUNBUFFERED 1

# activate virtual environment
ENV FLASK_APP='app'
ENV FLASK_ENV='development'
ENV FLASK_DEBUG=1
ENV MASTER_DB_NAME=${MASTER_DB_NAME}
ENV MASTER_DB_USER=${MASTER_DB_USER}
ENV MASTER_DB_PASSWORD=${MASTER_DB_PASSWORD}
ENV MASTER_DB_HOST=${MASTER_DB_HOST}
ENV MASTER_DB_PORT=${MASTER_DB_PORT}
ENV MASTER_DB_LOG_MODE=${MASTER_DB_LOG_MODE}

#Command to run the executable
CMD ["flask", "run","--host=0.0.0.0"]