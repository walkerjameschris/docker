# Base image
FROM ollama/ollama

# Define long context version of Mistral Nemo
RUN echo "FROM mistral-nemo:12b" >> /tmp/Modelfile
RUN echo "PARAMETER temperature 0.25" >> /tmp/Modelfile
RUN echo "PARAMETER num_ctx 16384" >> /tmp/Modelfile

# Pull models
RUN ollama serve
RUN ollama create mistral-nemo:12b-16k -f /tmp/Modelfile
RUN ollama pull mxbai-embed-large
