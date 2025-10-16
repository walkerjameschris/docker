# Base image
FROM continuumio/miniconda3

# Install packages
RUN pip install torch --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install jupyterlab-lsp "python-lsp-server[all]" mypy
RUN apt-get update && apt-get install curl
RUN curl -LsSf https://aider.chat/install.sh | sh

# Workspace settings
RUN conda init bash
COPY overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json
WORKDIR /home/jovyan/work/
EXPOSE 8888

# Run image
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
