# Use a Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install Firefox
RUN apt-get update && apt-get install -y firefox-esr
RUN apt-get update && apt-get install -y wget curl

# Install wget
RUN apt-get install -y wget

# Get the latest GeckoDriver version
RUN LATEST_GECKODRIVER_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
#RUN curl -sSL https://github.com/mozilla/geckodriver/releases/download/$LATEST_GECKODRIVER_VERSION/geckodriver-$LATEST_GECKODRIVER_VERSION-linux64.tar.gz | tar -xz -C /usr/local/bin

# Download and extract the latest GeckoDriver version
RUN echo "Latest geckodriver version is: $LATEST_GECKODRIVER_VERSION"
RUN wget https://github.com/mozilla/geckodriver/releases/download/${LATEST_GECKODRIVER_VERSION}/geckodriver-${LATEST_GECKODRIVER_VERSION}-linux64.tar.gz
RUN tar -xvzf geckodriver-${LATEST_GECKODRIVER_VERSION}-linux64.tar.gz -C /usr/local/bin
RUN rm geckodriver-${LATEST_GECKODRIVER_VERSION}-linux64.tar.gz


# Remove wget
RUN apt-get purge -y wget

# Clean up
RUN rm -rf /var/lib/apt/lists/*
# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV FIREFOX_DRIVER_PATH=/usr/local/bin/geckodriver

# Run test file when the container launches
CMD ["python", "-m", "unittest", "tests.automation.selenium_automation_tests"]
