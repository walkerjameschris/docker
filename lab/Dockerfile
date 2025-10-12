# ./python-dev/Dockerfile
FROM python:3.12-slim

# Set up a working directory
WORKDIR /workspace

# Install basic dev tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Optional: pre-install common Python tools
RUN pip install --no-cache-dir pip setuptools wheel

# Expose port for Positron or HTTP dev server
EXPOSE 8000

# Start a simple shell on container run (override with your own CMD if needed)
CMD [ "tail", "-f", "/dev/null" ]
