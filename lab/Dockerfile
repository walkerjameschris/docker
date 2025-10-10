FROM continuumio/miniconda3
USER root
RUN useradd -ms /bin/bash vscode
RUN chown -R vscode:users /home/vscode
RUN chown -R vscode:users /opt/conda
RUN mkdir -p /home/vscode/Documents
USER vscode
ENV PATH="/opt/conda/bin:${PATH}"
RUN pip install plotnine polars pyarrow scikit-learn gh ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
ENV SHELL=/bin/bash
ENV TERM=xterm-256color
WORKDIR /home/vscode/Documents
USER vscode
CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
