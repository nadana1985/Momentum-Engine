# ==============================================================================
# KRONOS V12 STANDALONE DOCKERFILE (AWS ECS / FARGATE / EC2 DOCKER READY)
# ==============================================================================
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    OMP_NUM_THREADS=1 \
    OPENBLAS_NUM_THREADS=1 \
    SCIPY_OPENBLAS64_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 \
    VECLIB_MAXIMUM_THREADS=1 \
    NUMEXPR_NUM_THREADS=1 \
    NICEGUI_HOST=0.0.0.0 \
    NICEGUI_PORT=8056

WORKDIR /app

# Install minimal OS dependencies for network & compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pinned Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Ensure pipeline scripts are executable
RUN chmod +x pipeline_v12.sh

# Expose NiceGUI Command Center Dashboard
EXPOSE 8056

# Healthcheck to verify dashboard responsiveness
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD curl -f http://localhost:8056/ || exit 1

# Default command: Start NiceGUI Command Center Dashboard
CMD ["python", "momentum_v12/dashboard_nicegui.py"]
