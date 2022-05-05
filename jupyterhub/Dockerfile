FROM jupyter/base-notebook:python-3.8.8

USER root

RUN apt-get update && \
    apt-get install -y git

USER $NB_UID

RUN python -m pip install --upgrade pip && \
    python -m pip install carla==0.9.12 ipywidgets voila \
                          nbgitpuller jupyter-server-proxy
