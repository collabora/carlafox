FROM jupyter/base-notebook:python-3.8.8

USER root

RUN apt-get update && \
    apt-get install -y git

USER $NB_UID

RUN python -m pip install --upgrade pip && \
    python -m pip install carla==0.9.12 ipywidgets voila \
                          nbgitpuller 'nbclassic>=0.2.8'

# RUN apt-get update && \
#     DEBIAN_FRONTEND=noninteractive \
#         apt-get install -y git curl wget jq sudo unzip \
#                            libpng16.16 libtiff-dev libtiff5 libgl1-mesa-glx python3-tk && \
#     pip3 install --upgrade pip jedi jupyter voila && \
#     pip3 install traitlets==5.1.1 pygments==2.4.1 && \
#     pip3 install -r requirements.txt && \
#     python3 -m easy_install --no-deps carla-0.9.11-py3.7-linux-x86_64.egg && \
#     pip3 install -r carla-requirements.txt && \
#     rm carla-0.9.11-py3.7-linux-x86_64.egg

# RUN conda install 
# RUN curl -o /usr/local/bin/mc https://dl.min.io/client/mc/release/linux-amd64/mc && \
#     chmod a+x /usr/local/bin/mc

WORKDIR /notebooks

CMD ./start-jupyter.sh
