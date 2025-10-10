FROM continuumio/miniconda3

RUN conda init bash
ENV SHELL=/bin/bash
ENV TERM=xterm-256color

RUN pip install jupyterlab plotnine polars pyarrow scikit-learn gh ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab-lsp 'python-lsp-server[all]' mypy
RUN apt-get update && apt-get install -y build-essential cmake libsfml-dev
RUN conda install --channel conda-forge --yes r-base r-tidyverse
RUN Rscript -c "install.packages('IRkernel'); IRkernel::installspec(user = TRUE)"

RUN useradd -m lab
USER lab
WORKDIR /home/lab/mnt/

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
