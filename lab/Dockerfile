# Base image
FROM continuumio/miniconda3

# Install packages
RUN pip install torch --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama jupyter_rfb
RUN pip install jupyterlab-lsp "python-lsp-server[all]" mypy "jupyter-ai[all]"

# Workspace settings
RUN conda init bash
COPY overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json
COPY config.json /root/.local/share/jupyter/jupyter_ai/config.json
WORKDIR /home/jovyan/work/
EXPOSE 8888

# Run image
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
