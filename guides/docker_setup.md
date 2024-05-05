# Docker Setup, usage and installation

Section of the Course - INDEX:4 [Building a Django Docker Container](https://www.youtube.com/watch?v=PkynrL1aU9o&list=PLOLrQ9Pn6cayGytG1fgUPEsUp3Onol8V7&index=4)

## Install Docker without Docker Desktop (this one)
- [WSL 2 with Docker w/o Docker Desktop (Youtube)](https://www.youtube.com/watch?v=SDk3pqFXgs8)
- [Ubuntu Install guide](https://docs.docker.com/engine/install/ubuntu/)
- Steps:
    1. Run to install
    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh ./get-docker.sh --dry-run
    ```
    2. optional: [linux-postinstall](https://docs.docker.com/engine/install/linux-postinstall/)
    3.  docker run hello-world
- Trouble Shooting: Fix from [Docker Forum The savior!! quangsangle](https://forums.docker.com/t/wsl-cannot-connect-to-the-docker-daemon-at-unix-var-run-docker-sock-is-the-docker-daemon-running/116245/6#:~:text=1%20month%20later-,quangsangle,-Jul%202023):
    Run 
    ```bash
    sudo update-alternatives --config iptables
    ```
    Enter 1 to select iptables-legacy, Now run sudo service docker start, and Docker will start as expected!
- install docker compose: https://docs.docker.com/compose/install/linux/


## Useful commands
- test docker install: ```docker run hello-world```
- start docker: ```sudo service docker start``` or ```sudo systemctl start docker```
- stop docker: ```sudo service docker stop``` or ```sudo systemctl stop docker```
- check docker processes: ```docker ps```
- check docker images: ```docker images```
- check docker logs: ```docker logs <container_id>```
- build docker image where the Dockerfile Exist: ``` docker compose up -d --build```
- stop docker container: ```docker stop <container_id>```
- enable Auto Start 
    ```bash
    sudo systemctl enable docker.service
    sudo systemctl enable containerd.service
    ```
- disable Auto Start
    ```bash
    sudo systemctl disable docker.service
    sudo systemctl disable containerd.service
    ```