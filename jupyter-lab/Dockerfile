# Use a NVIDIA CUDA base image for GPU support
FROM nvidia/cuda:12.8.0-base-ubuntu24.04

# Install Miniconda
ENV PATH="/opt/conda/bin:${PATH}"
RUN apt-get update && apt-get install -y --no-install-recommends wget curl bzip2 ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && /bin/bash /tmp/miniconda.sh -b -p /opt/conda \
    && rm /tmp/miniconda.sh

# Install the necessary libraries via conda-forge
RUN conda install -c conda-forge polars pytorch-cuda=12.8 plotnine jupyterlab -y

# Set the working directory
WORKDIR /app

# Expose port for JupyterLab
EXPOSE 8888

# Command to run JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]

