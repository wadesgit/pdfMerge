FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir PyPDF2

# Command to run your script
CMD ["python", "main.py"]