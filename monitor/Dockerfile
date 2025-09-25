# TODO: Dockerhub is down, use `FROM continuumio/miniconda3` later
FROM mcr.microsoft.com/devcontainers/miniconda:3
WORKDIR /app
RUN pip install shiny
RUN apt install coreutils
COPY app.py .
EXPOSE 8000
CMD ["shiny", "run", "--host", "0.0.0.0", "--port", "8000"]
