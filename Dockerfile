# Base stage with common setup
FROM python:3.12-slim as base

# Install system dependencies required for WeasyPrint
RUN apt-get update \
    && apt-get install -y \
    python3-pip \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy pyproject.toml and uv.lock
COPY pyproject.toml uv.lock ./

# Test stage - includes dev dependencies
FROM base as test

# Install Python dependencies including dev dependencies for testing
RUN uv sync \
    --locked \
    --no-install-project

# Copy files and install project
COPY src/ ./src/
COPY tests/ ./tests/
COPY README.md ./
RUN uv sync \
    --locked \
    --no-editable

# Production stage - only runtime dependencies
FROM base as production

# Install only production dependencies
RUN uv sync \
    --locked \
    --no-dev \
    --no-install-project

# Copy files and install project
COPY src/ ./src/
COPY README.md ./
RUN uv sync \
    --locked \
    --no-dev \
    --no-editable

# Set the default command
CMD ["uv", "run", "--no-dev", "generate-pdf"]
