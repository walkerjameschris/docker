# Base image
FROM ubuntu:24.04

# Install necessary tools, download and silently install Miniconda to /opt/conda
RUN apt-get update && apt-get install -y wget bzip2 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm -f /tmp/miniconda.sh

# Make the 'conda' command available globally
ENV PATH="/opt/conda/bin:$PATH"

# Install packages
RUN pip install torch --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install jupyterlab-lsp "python-lsp-server[all]" mypy "jupyter-ai[all]"

# Workspace settings
RUN conda init bash
COPY overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json
COPY config.json /root/.local/share/jupyter/jupyter_ai/config.json
WORKDIR /home/jovyan/work/
EXPOSE 8888

# Render pipeline
RUN apt-get update
RUN apt-get install -y libegl1-mesa-dev libgl1-mesa-dri libxcb-xfixes0-dev mesa-vulkan-drivers
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
RUN conda install -c conda-forge libjpeg-turbo
RUN pip install jupyter_rfb simplejpeg pygfx
ENV PYGFX_WGPU_ADAPTER_NAME="llvmpipe"

# Run image
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
