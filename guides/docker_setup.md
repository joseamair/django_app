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

## The Dockerfile
- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
It has the recipe to build the docker image. It is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession.

## The Docker Compose File
- [Docker Compose reference](https://docs.docker.com/compose/compose-file/)
- It is a YAML file that defines how Docker containers should behave in production. It is used to define and run multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.


## The Don't forget of Docker setup
- when creating the entrypoint.sh file, make sure to give it the right permissions
    ```bash
    chmod +x entrypoint.sh
    ```
- when creating the Dockerfile, make sure to give it the right permissions
    ```bash
    chmod +x Dockerfile
    ```

## Useful commands
- test docker install: ```docker run hello-world```
- start docker: ```sudo service docker start``` or ```sudo systemctl start docker```
- stop docker: ```sudo service docker stop``` or ```sudo systemctl stop docker```
- check docker processes: ```docker ps```
- check docker images: ```docker images```
- check docker logs: ```docker logs <container_id>```
- build docker image where the Dockerfile exists: ``` docker compose up -d --build```
- stop docker container: ```docker stop <container_id>```
- shut down all active containers: ```docker stop $(docker ps -a -q)``` 
- open and run a command in a container: ```docker exec -it <container_id> bash```
- check logs of a container: ```docker logs <container_id or container name>```
- check logs live of a container: ```docker logs -f <container_id or container name>```
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

## Extra useful commands
- check registered celery tasks running inside the container: ```docker logs celery | grep '\[tasks\]' -A2```