FROM mcr.microsoft.com/devcontainers/python:0-3.10
# FROM pytorch/pytorch
# FROM pytorch/pytorch:2.1.2-cuda12.1-cudnn8-devel


RUN apt-get update && apt install git-lfs -y
# RUN apt install cuda -y


RUN python -m pip install --upgrade pip \
    && python -m pip install 'flit>=3.8.0'

ENV FLIT_ROOT_INSTALL=1

COPY pyproject.toml .
RUN touch README.md \
    && mkdir -p src/ant_colony_bench \
    && python -m flit install --only-deps --deps develop \
    && rm -r pyproject.toml README.md src
