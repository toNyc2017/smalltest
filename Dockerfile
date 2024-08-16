# Use an official Python runtime as a parent image
FROM python:3.8


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define a build-time argument
ARG AZURE_STORAGE_ACCOUNT_KEY
ARG OPENAI_API_KEY

# Set the environment variable using the build-time argument
ENV AZURE_STORAGE_ACCOUNT_KEY=${AZURE_STORAGE_ACCOUNT_KEY}

ENV OPENAI_API_KEY=${OPENAI_API_KEY}


# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
