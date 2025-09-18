# Start from a clean, minimalist CUDA base image for CUDA 12.8
FROM nvidia/cuda:12.4.1-base-ubuntu22.04

# Install python
RUN apt-get install -y --no-install-recommends python3.12
RUN apt-get install -y --no-install-recommends python3-pip
RUN pip install jupyterlab

# Install PyTorch and its dependencies from the official nightly build URL
# The `pip` command will fetch the pre-compiled wheel for CUDA 12.8
RUN pip install --pre torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/nightly/cu128

# Set the working directory and expose the port
WORKDIR /app
EXPOSE 8888

# Command to start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
