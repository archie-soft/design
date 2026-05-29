# Multi-stage build for docs-service
FROM python:3.12-slim as builder

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.12-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY src/docs_service.py .

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=docs_service.py

# Health check
# HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD python -c "import requests; requests.get('http://localhost:5000/api/health')" || exit 1

# Expose port
EXPOSE 5000

# Run the Flask application
CMD ["python", "docs_service.py"]
