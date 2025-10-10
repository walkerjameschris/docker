FROM continuumio/miniconda3
RUN pip install plotnine polars pyarrow scikit-learn gh ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
ENV SHELL=/bin/bash
ENV TERM=xterm-256color
WORKDIR /home/vscode/Documents
