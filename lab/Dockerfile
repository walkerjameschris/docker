# Start from a clean, minimalist CUDA base image for CUDA 12.8
FROM nvidia/cuda:12.4.1-base-ubuntu22.04

# Install necessary packages and clean up
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    python3.12 \
    python3.12-distutils \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install PyTorch and its dependencies from the official nightly build URL
# The `pip` command will fetch the pre-compiled wheel for CUDA 12.8
RUN pip install --pre torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/nightly/cu128

# Install JupyterLab
RUN pip install jupyterlab

# Set the working directory and expose the port
WORKDIR /app
EXPOSE 8888

# Command to start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
