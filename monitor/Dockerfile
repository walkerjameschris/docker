FROM python:3.13
WORKDIR /app
RUN pip install shiny
COPY app.py .
EXPOSE 8000
CMD ["shiny", "run", "--host", "0.0.0.0", "--port", "8000"]

