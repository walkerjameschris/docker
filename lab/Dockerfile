FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN useradd -m lab
USER lab
WORKDIR /home/lab/Documents
RUN mkdir -p /home/lab/.config/code-server
RUN echo '{ "terminal.integrated.shell.linux": "/bin/bash", "terminal.integrated.shellArgs.linux": ["-l", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate base && exec bash"] }' > /home/lab/.config/code-server/settings.json
EXPOSE 8080
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]
