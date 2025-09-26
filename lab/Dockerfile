FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | sudo bash -
RUN sudo apt-get install -y nodejs
RUN curl -fsSL https://code-server.dev/install.sh | sh
EXPOSE 8080
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]
WORKDIR /home/lab/Documents
