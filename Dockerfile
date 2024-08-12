# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn


# Install dependencies from requirements.txt
#COPY requirements.txt /app/
#RUN pip install -r requirements.txt



# Make port 80 available to the world outside this container
EXPOSE 80

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
