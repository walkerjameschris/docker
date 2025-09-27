# Base image
FROM ubuntu:24.04

# Install Miniconda to /root/miniconda3
RUN apt-get install curl 
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
RUN bash miniconda.sh -b -p /root/miniconda3 &&
RUN rm miniconda.sh

# Add conda to PATH
ENV PATH="/root/miniconda3/bin:$PATH"

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Python packages into (base) conda env
RUN pip install plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129

# Install code-server extensions
RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-pyright.pyright
RUN code-server --install-extension ms-toolsai.jupyter

# Copy VSCode settings
COPY settings.json /root/.local/share/code-server/User/settings.json

# Expose code-server port
EXPOSE 8080

# Run code-server
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]
