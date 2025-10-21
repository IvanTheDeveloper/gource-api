FROM python:3.11-slim

# Avoid __pycache__ and .pyc files generation
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    gource \
    ffmpeg \
    xvfb \
    xauth \
    && rm -rf /var/lib/apt/lists/*

# Create working dir
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy app code
COPY . .

# Create a non-root user to run the application
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser \
    && chown -R appuser:appgroup /app
USER appuser

# Define default port, can be overridden at runtime
ARG PORT=8080
EXPOSE ${PORT}

# Define entrypoint and default command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "run.py"]
