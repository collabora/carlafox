# The CARLA🚖&nbsp;&nbsp;💜&nbsp;&nbsp;ROS🦾&nbsp;&nbsp;💜&nbsp;&nbsp;Foxglove📊 demo

## Requirements

The demo requires an NVIDIA GPU, the NVIDIA container runtime and docker-compose v1.28.0+.
You can check for these dependencies by running:

```console
$ docker info |grep Runtimes:
Runtimes: io.containerd.runc.v2 io.containerd.runtime.v1.linux nvidia runc
$ docker-compose version --short
1.29.2
```

Currently the system only works on `linux/x86_64` machines (mostly because of the CARLA server).

## Quickstart

How to (re)start the system:

```bash
docker-compose rm -sf && docker-compose pull && docker-compose up -d --build --force-recreate
```

Afterwards navigate to [http://localhost:8080](http://localhost:8080) to explore the system.

## Hacking

If you wish to hack on the intro notebook (or borrow the ideas for your own project) make sure you use
the `cleanup-notebook.py` tool before commiting your changes. It clears the outputs cells leaving only
the ones marked with `#keep-output` (our UI buttons) and also does a metadata cleanup to keep the Git
history useful and avoid trivial merge conflicts (you can read more about the latter in
[the nbdev documentation](https://nbdev.fast.ai/clean.html)).

```bash
python3 -m pip install -r dev-requirements.txt
python3 cleanup-notebook.py notebooks/CARLA\ 💜\ Foxglove\ demo.ipynb
```
