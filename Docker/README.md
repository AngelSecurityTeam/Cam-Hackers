# Run ZPhiSher in Docker Compose

![docker](https://img.shields.io/badge/Docker-v19.03.12-blue?style=plastic&logo=docker)
![dockercompose](https://img.shields.io/badge/Docker_Compose-v1.25.4-orange?style=plastic&logo=docker)
![Maintainer](https://img.shields.io/badge/Maintainer-Equinockx-success?style=plastic&logo=terraform)

## Requeriments

- [X] Docker
- [X] docker-compose

## Usage Mode

Clone the repo from Github
```bash
git clone https://github.com/AngelSecurityTeam/Cam-Hackers
cd Cam-Hackers
```

Run docker-compose

```bash
docker-compose up --build -d
```
'_Don not need redirection of ports 'cause the container is exposed to internet_' <br>

Verify of the container is running with:

```bash

equinockx~$ docker-compose ps

Name          Command           State   Ports
---------------------------------------------
camm   python3 cam-hackers.py   Up           
          

```
Get the container ID

```bash
equinockx~$ docker ps -l

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
6ff436e76ab7        cammhack:v0.1       "python3 cam-hackers…"   2 minutes ago       Up 2 minutes                            camm

```
Executing Cam-Hackers inside of container

```bash
docker exec -ti 6ff436e76ab7 python3 cam-hackers.py
```

## First Start the services

```bash
docker-compose up --build -d
```
## Down the container
```bash
docker-compose down
```
## Stop the services

```bash
docker-compose stop
```
## Start the services

With this command docker-compose will initialize the service stopped

```bash
docker-compose start
```