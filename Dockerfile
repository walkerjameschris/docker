FROM quay.io/jupyter/pytorch-notebook:cuda12-python-3.11.8
RUN pip install polars plotnine pyarrow
RUN pip install jupyterlab-lsp "python-lsp-server[all]" mypy jupyter-ai

