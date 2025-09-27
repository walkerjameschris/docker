# Base image
FROM continuumio/miniconda3

# Termainl, system dependencies, and Code Server
RUN apt-get update && apt-get install -y curl zsh
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Python packages + special index for CUDA PyTorch
RUN pip install plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN conda install -y ipython

# Create user
RUN useradd -m -s /bin/zsh lab
RUN mkdir -p /home/lab/.local/share/code-server
RUN mkdir -p /home/lab/.config

# Switch to the lab user
USER lab
WORKDIR /home/lab/Documents

# Apply user settings
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> /home/lab/.zshrc
RUN echo "conda activate base" >> /home/lab/.zshrc
COPY settings.json /home/lab/.local/share/code-server/User/settings.json

# Install extensions as the lab user to avoid permission errors
RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-pyright.pyright
RUN code-server --install-extension ms-toolsai.jupyter

# Run the server
EXPOSE 8080
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]
