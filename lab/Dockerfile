FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow
RUN pip install torch
WORKDIR /home/jovyan/Documents
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
