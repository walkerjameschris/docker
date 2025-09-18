FROM nvidia/cuda:12.4.1-base-ubuntu22.04

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py312_24.1.2-0-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh

ENV PATH="/opt/conda/bin:$PATH"

RUN conda install -c pytorch -c nvidia -y pytorch torchvision torchaudio pytorch-cuda=12.1 jupyterlab && \
    conda clean -tipsy

WORKDIR /app

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
