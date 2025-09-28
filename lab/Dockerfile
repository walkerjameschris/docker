FROM continuumio/miniconda3
RUN useradd -ms /bin/bash jovyan
USER jovyan
WORKDIR /home/jovyan
RUN conda init bash
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn gh
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab_theme_solarized_dark jupyterlab-lsp 'python-lsp-server[all]' mypy
ENV SHELL=/bin/bash \
    TERM=xterm-256color
WORKDIR /home/jovyan/Documents
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--LabApp.token=''", "--allow-root"]
