# Build stage
FROM python:3.10-slim as builder

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Final stage
FROM python:3.10-slim

# Create a non-root user
RUN addgroup --system app && adduser --system --group app

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy only necessary files from builder
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install Python packages from wheels
RUN pip install --no-cache /wheels/* \
    && rm -rf /wheels

# Create necessary directories and set permissions
RUN mkdir -p /tmp/logs && \
    chown -R app:app /tmp/logs && \
    chmod -R 755 /tmp/logs

# Copy application code
COPY --chown=app:app . .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create log directory with correct permissions
RUN mkdir -p /tmp/logs && \
    chown -R app:app /tmp/logs && \
    chmod -R 755 /tmp/logs

# Create a startup script
RUN echo '#!/bin/sh\n\
# Start FastAPI server in the background\
uvicorn main:app --host 0.0.0.0 --port 8000 &\
\
# Start the Discord bot\
python -c "from main import bot, Config; import asyncio; asyncio.run(bot.start(Config.DISCORD_TOKEN))"\
\
# Keep the container running\
wait\n' > /startup.sh && \
    chmod +x /startup.sh && \
    chown app:app /startup.sh

# Set the working directory and user
WORKDIR /app
USER app

# Expose the port the app runs on
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Command to run the application
CMD ["/startup.sh"]
