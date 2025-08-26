FROM python:3.12-slim

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

# Install Python dependencies using uv
RUN uv sync \
    --locked \
    --no-dev \
    --no-install-project

# Copy application files
COPY src/ ./src/
COPY README.md ./
RUN uv sync \
    --locked \
    --no-dev \
    --no-editable

# Create output directory
RUN mkdir -p /app/output

# Set the default command
# TODO: get 'uv run generate-pdf' to work
CMD ["uv", "run", "--no-dev", "python", "src/profile/generate_pdf.py"]
