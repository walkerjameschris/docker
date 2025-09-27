# Base image
FROM continuumio/miniconda3

# Termainl, system dependencies, and Code Server
RUN apt-get update && apt-get install -y curl zsh
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Python packages + special index for CUDA PyTorch
RUN pip install plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129

# Create user
RUN useradd -m -s /bin/zsh lab
USER lab
WORKDIR /home/lab/Documents

# Apply user settings
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> /home/lab/.zshrc
RUN echo "conda activate base" >> /home/lab/.zshrc
COPY settings.json /home/lab/.local/share/code-server/User/settings.json
COPY extensions.txt /home/lab/extensions.txt

# Install extensions and fix ownership
RUN mkdir -p /home/lab/.local/share/code-server/User
RUN cat /home/lab/extensions.txt | while read ext; do code-server --install-extension "$ext"; done
RUN chown -R lab:lab /home/lab

# Run the server
EXPOSE 8080
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]
