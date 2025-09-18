# Use the official NVIDIA CUDA base image for PyTorch with a specific Ubuntu version and CUDA toolkit.
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# Install JupyterLab and clean up unnecessary files to reduce image size.
RUN pip install jupyterlab

# Set the working directory inside the container.
WORKDIR /app

# Expose port 8888 for JupyterLab.
EXPOSE 8888

# Command to start JupyterLab with specific settings for containerized use.
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
