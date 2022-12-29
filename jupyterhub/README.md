# How to setup the Carlafox demo system

## Install microk8s

It's unclear if `--channel=1.22` is required.

    sudo snap install microk8s --classic --channel=1.22
    sudo usermod -a -G microk8s "$USER"
    newgrp microk8s
    microk8s status --wait-ready
    microk8s enable community
    microk8s enable dns storage gpu traefik

Verify GPU availability inside K8s with

    microk8s.kubectl get nodes -o=custom-columns=NAME:.metadata.name,GPUs:.status.capacity.'nvidia\.com/gpu'


## Install the Carlafox helm chart

Edit `config.yaml` and fill in the GitHub auth secret tokens. Afterwards enable the jupyterhub helm repo and deploy carlafox:

    microk8s.helm3 repo add jupyterhub https://jupyterhub.github.io/helm-chart/
    microk8s.helm3 repo update

    microk8s.helm3 upgrade --cleanup-on-fail   --install carlafox jupyterhub/jupyterhub   --namespace carlafox   --create-namespace   --version=1.2.0   --values carlafox-config.yaml
