# Base image
FROM continuumio/miniconda3

# Install packages
RUN pip install torch --index-url https://download.pytorch.org/whl/cu129
RUN pip install plotnine polars pyarrow scikit-learn ollama

# Workspace settings
RUN conda init bash
RUN apt-get update && apt-get install -y curl unzip micro tmux
RUN curl -fsSL https://opencode.ai/install | bash
COPY opencode.json /root/.config/opencode/opencode.json
COPY settings.json /root/.config/micro/settings.json
WORKDIR /home/Documents/

# Run image
CMD ["/bin/bash"]
