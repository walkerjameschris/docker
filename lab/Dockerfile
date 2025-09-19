FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars
COPY overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
