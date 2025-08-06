# KCNA (Kubernetes and Cloud Native Associate)

Best to start kubernetes journey from KCNA as it builds the required concepts and architecture level view of its components.

> Pre-requisites for KCNA:

- RHEL - Linux 
- Docker

> Re-cap of some related concepts:

## Docker (for Detailed - see Docker notes)

- Open-source centralized platform 
- Designed to create and deploy applications
- Was first released in March 2013 and developed by **SOLOMON HYKES** and **SEBESTIAN PHAL**
- Docker is written in "**GO**" language
- It is an example of PAAS
- Uses containers on the host OS to run applications
- Allows applications to use same linux kernel of host OS
- Docker can be installed on any OS but docker engine runs natively on Linux Distros
- It does OS level (in contrary to VM's hardware level) virtualization - containerzation.

### Advantages of Docker

- No pre-allocation of memory
- Lightweight
- Take less time to deploy application
- Can run over physical hardware and clouds
- Image can be resued for mutiple deployments

### Disdvantages of Docker

- Not good solution of GUI rich applications
- A bit hard to manage
- Doesn't support cross platfarm environment (image exported from `Linux` will not run in `windows`)
- Doesn't support across different linux distors (image from `Ubuntu` - will not run in `Centos`)

### Components of Docker

1. Docker Daemon/Engine

- Runs on host OS
- Responsible for running containers to manage services/apps
- Can communicate with other engines/daemons

2. Docker Client

- Docker users interact with docker engine via docker client
- It uses commands and rest APIs to communicate to docker engine
- When a user runs a command on server (client), it goes to docker engine and is processed by docker engine/daemon.
- Can communicate with more than one engine.

3. Docker Host

- Provides an environmnet to execute and run applications
- Contains docker engine, images, containers, networks, volumes, etc.

### Installing Docker and a bit hands-on

- `apt-get update`
- `apt-get install docker -y`
- `docker -v`
- `systemctl enable docker`
- `docker run hello-world`
- `docker ps -a`
- `docker system prune`

> Orchestration Tools

There are three major orchestration tools:

1. Docker Swarm (easy to deploy but for smaller applications only)
2. Kubernetes (most widely used due to compatibility with multiple clouds and open-source community)
3. MESOS (of Apache)


## **Kubernetes Architecture**

Here is a brief overview of components of kubernetes which are created when in our host when we configure kubernetes.

### 1. API Server

- It acts as a frontend/interface for all communcation between different components of kubernetes and external interactions with k8s.

> What is **CRI**? | Container Runtime Interface



### 2. ETCD

- Distrubuted and reliable storage in k8s, that stores data in key-value format and manages the cluster.
- Implements logs and prevents conflicts in-case of there are multuple masters in a cluster.

### 3. Controller Manager

- It is the brain of orchestration.
- It maintains the required state, number of containers and created new as soon as some goes down.

### 4. Scheduler

- After controller has created the new containers, it decides where to (in which node) place that container.

### 5. Container Runtime

- Provides the runtime for containers.
- For example, incase of kubernetes, we use docker as container runtime.

### 6. Kubelet

- This component of kubernetes runs on each node of the entire cluster and makes sure that the containers are rinning on the nodes as expected (according to configurations of kubelet)

