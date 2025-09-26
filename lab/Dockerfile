FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
WORKDIR /home/lab/Documents
EXPOSE 22
