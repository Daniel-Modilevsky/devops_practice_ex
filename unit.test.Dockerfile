# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Firefox and GeckoDriver
#RUN apt-get update && apt-get install -y firefox-esr && \
#    wget -O geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz && \
#    tar -xzf geckodriver.tar.gz && \
#    mv geckodriver /usr/local/bin/ && \
#    chmod +x /usr/local/bin/geckodriver && \
#    rm geckodriver.tar.gz


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the unit tests
CMD ["python", "-m", "unittest", "tests.unit.test_dashboard"]
