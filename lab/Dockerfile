# Use an official NVIDIA CUDA base image for Ubuntu 24.04 with CUDA 13.x
# The 'runtime' variant is sufficient as it includes the necessary libraries for running PyTorch.
FROM nvidia/cuda:13.0.1-runtime-ubuntu24.04

# Install Python and its dependencies via apt-get
# We use a single RUN command to minimize the number of layers
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.12 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Jupyter Lab and PyTorch with GPU support
# We use pip here to install PyTorch directly from the PyTorch nightlies for CUDA 13,
# as a stable release might not be available yet.
# Note: You may need to replace the URL with the correct one if the nightly build structure changes.
RUN pip3 install --no-cache-dir \
    jupyterlab \
    torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/nightly/cu130

# Command to run Jupyter Lab
CMD ["jupyter-lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
