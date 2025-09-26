FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow scikit-learn ollama
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
RUN pip install jupyterlab-theme-solarized-dark
RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/
RUN echo '{"theme": "Solarized Dark"}' > /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.json
WORKDIR /home/jovyan/Documents
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
