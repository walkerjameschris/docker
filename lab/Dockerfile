FROM continuumio/miniconda3

# Install core Python packages
RUN pip install \
    jupyterlab \
    plotnine \
    polars \
    pyarrow \
    scikit-learn \
    gh \
    jupyterlab-lsp \
    python-lsp-server[all]

# Install PyTorch with CUDA 12.9
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129

# Install Node.js and Pyright (for LSP support)
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g pyright && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Solarized Dark theme for JupyterLab
RUN jupyter labextension install @ryantam626/jupyterlab_solarized_dark

# Copy user preferences (must match JupyterLab's expected location)
COPY overrides.json /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

# Set working directory
WORKDIR /home/jovyan/Documents

# Expose JupyterLab port
EXPOSE 8888

# Start JupyterLab with no token (for dev use only)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
