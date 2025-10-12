FROM continuumio/miniconda3
RUN pip install torch --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install jupyterlab-lsp "python-lsp-server[all]" mypy "jupyter-ai[all]"
RUN conda init bash
ENV SHELL=/bin/bash
WORKDIR /home/jovyan/work/
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
