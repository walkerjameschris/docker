FROM continuumio/miniconda3
RUN pip install chatlas shinychat shiny
WORKDIR /app
COPY app.py .
EXPOSE 80
CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "80"]
