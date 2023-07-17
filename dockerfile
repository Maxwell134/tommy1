# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /main

# Copy the Python requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the Python code into the container
COPY main.py .

# Expose the port on which the Flask app will run (optional)
EXPOSE 5000

# Set the command to run when the container starts
CMD ["python", "main.py"]
