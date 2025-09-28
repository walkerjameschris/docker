# Base image
FROM continuumio/miniconda3

# Update system and install necessary packages (curl, zsh)
RUN apt-get update && apt-get install -y --no-install-recommends curl zsh gh

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Python packages + special index for CUDA PyTorch
RUN pip install plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129

# Install extensions (these will be installed for the root user)
RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-pyright.pyright

# Configure root's shell to automatically activate the conda base environment
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> /root/.zshrc
RUN echo "conda activate base" >> /root/.zshrc

# Copy the settings.json file to root's configuration directory
COPY settings.json /root/.local/share/code-server/User/settings.json

# Expose the default port
EXPOSE 8080

# Run the server as the root user
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]
