FROM continuumio/miniconda3
RUN pip install plotnine polars pyarrow scikit-learn gh ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN apt-get update && apt-get install -y build-essential cmake libsfml-dev
RUN conda install --channel conda-forge --yes r-base r-tidyverse
ENV SHELL=/bin/bash
ENV TERM=xterm-256color
WORKDIR /home/vscode/Documents
CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
