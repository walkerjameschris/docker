FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN apt-get update && apt-get install -y curl zsh git
RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN useradd -m -s /bin/zsh lab
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> /home/lab/.zshrc
RUN echo "conda activate base" >> /home/lab/.zshrc
USER lab
WORKDIR /home/lab/Documents
EXPOSE 8080
CMD ["bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && code-server --bind-addr 0.0.0.0:8080 --auth none"]
