FROM continuumio/miniconda3
RUN pip install jupyterlab plotnine polars pyarrow
RUN pip install torch --index-url https://download.pytorch.org/whl/cu121
RUN git config --global user.name ${GITHUB_USERNAME}
RUN git config --global user.password ${GITHUB_PAT}
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--LabApp.token=''"]
