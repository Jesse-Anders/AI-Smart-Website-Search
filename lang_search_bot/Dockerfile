# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements first, install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Now copy the rest of the application code
COPY . .


# Make port 6000 available to the world outside this container
EXPOSE 6000

# Run setup.py and app.py in the same session
CMD python lang_bot_build.py && python app.py