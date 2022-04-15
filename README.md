# The CARLA🚖&nbsp;&nbsp;💜&nbsp;&nbsp;ROS🦾&nbsp;&nbsp;💜&nbsp;&nbsp;Foxglove📊 demo

## Requirements

Requires docker-compose v1.28.0+, which you can verify by running:

```
docker-compose version
```

Currently the system only works on `linux/x86_64` machines (mostly because of the CARLA server).

## Quickstart

How to (re)start the system:

```
~/.local/bin/docker-compose rm -sf && ~/.local/bin/docker-compose pull && ~/.local/bin/docker-compose up -d --build --force-recreate
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
