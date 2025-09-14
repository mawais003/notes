

Google --- in 2014 --released-- Borg (old state of k8s) then open-sourced it later on...

## Kubernetes Architecture

It has two planes:

- Control Plane / Master Node
- Data Plane / Worker Node

### Control Plane

It consists of below important components:

- API Server: interface point to contact kubernetes cluster
- Scheduler: responsible for running pods
- Controller Manager: controls the entire cluster
- ETCD: acts as a key-value database 

### Data Plane

It consists of below important components:

- Kubeproxy: needed to access pods
- Kubelet : ensures all pods are running fine
- pods > deployments > services


> `kubectl` is a command line tool needed to interact with kubernetes cluster.