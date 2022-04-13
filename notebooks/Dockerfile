FROM jupyter/base-notebook:python-3.8.8

RUN python -m pip install --upgrade pip && \
    python -m pip install -vvv carla==0.9.12 ipywidgets voila

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

CMD jupyter nbclassic \
            --no-browser --allow-root \
            --ServerApp.port=8888 --ServerApp.ip=0.0.0.0 \
            --NotebookApp.allow_remote_access=True --NotebookApp.allow_origin='*' \
            --NotebookApp.base_url=notebooks --NotebookApp.password= --NotebookApp.token=
