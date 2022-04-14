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
