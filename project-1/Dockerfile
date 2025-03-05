# Use a minimal base image
FROM python:3.11-slim
 
# Set the working directory
WORKDIR /app
 
# Copy only necessary files first (better caching)
COPY requirements.txt .
 
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the rest of the application files
COPY . .
 
# Expose the port Flask runs on
EXPOSE 5000
 
# Define the command to run the application
CMD ["python", "app.py"]