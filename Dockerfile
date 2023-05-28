# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster
MAINTAINER jalotrashivam9@gmail.com
# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN python -m venv env && \
    . env/bin/activate && \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

CMD ["/bin/bash"]
