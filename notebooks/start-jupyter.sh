#!/bin/sh

jupyter trust ./*.ipynb
exec jupyter nbclassic \
    --no-browser --allow-root \
    --ServerApp.port=8888 --ServerApp.ip=0.0.0.0 \
    --NotebookApp.allow_remote_access=True --NotebookApp.allow_origin='*' \
    --NotebookApp.base_url=notebooks --NotebookApp.password= --NotebookApp.token=
