FROM continuumio/miniconda3
RUN pip install chatlas shinychat shiny shinyswatch
WORKDIR /app
COPY app.py .
COPY favicon.ico www/favicon.ico
EXPOSE 80
CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "80"]


