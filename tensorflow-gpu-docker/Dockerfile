FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/opt/conda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:${LD_LIBRARY_PATH}"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

# Copy environment.yml file
COPY environment.yml /tmp/

# Create conda environment
RUN conda env create -f /tmp/environment.yml

# Make the conda environment the default
RUN echo "conda activate tf" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Set up entry point to activate conda environment
WORKDIR /tf
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "tf"]
CMD ["/bin/bash"]