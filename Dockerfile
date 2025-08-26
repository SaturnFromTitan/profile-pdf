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
RUN uv sync --frozen

# Copy application files
COPY template.html .
COPY tailwind.css .
COPY generate_pdf.py .

# Create output directory
RUN mkdir -p /app/output

# Set the default command
CMD ["uv", "run", "python", "generate_pdf.py"]
