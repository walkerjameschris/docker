FROM continuumio/miniconda3
RUN conda init bash
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn gh
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab_theme_solarized_dark jupyterlab-lsp 'python-lsp-server[all]' mypy
ENV SHELL=/bin/bash
ENV TERM=xterm-256color
WORKDIR /home/jovyan/Documents
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
