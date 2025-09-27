FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN curl -fsSL https://code-server.dev/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /home/lab/Documents
EXPOSE 8888
CMD ["code-server", "--bind-addr", "0.0.0.0:8888", "--auth", "none"]
