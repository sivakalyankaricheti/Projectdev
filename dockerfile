# Step 1: Use official Python image
FROM python:3.13.0-alpine3.20

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy sum.py into container
COPY sum.py /app/

# Step 4: Keep container running
CMD ["tail", "-f", "/dev/null"]
