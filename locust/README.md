
# OUGN 2017, Spring Cruice, P78 - Locust
By Ove Olsen, ove.olsen@knowit.no

## About Locust
Website: http://locust.io

An open source load testing tool
Define user behaviour with Python code, and swarm your system with millions of simultaneous users.

Locust supports Python 2.7, 3.3, 3.4, 3.5, and 3.6.

## Demo Requirements
 - Docker version 1.11.1
 - Python
 - docker-locust https://github.com/hakobera/docker-locust
 - names https://github.com/treyhunner/names

## Dockerfile

```
#Dockerfile
FROM hakobera/locust
RUN easy_install names
ADD ./test /test
ENV SCENARIO_FILE /test/locustfile.py
```

## Writing tests
  - add test/locustfile.py
  - See http://docs.locust.io/en/latest/writing-a-locustfile.html for help.

## Build & Run standalone
```
#run.sh
#!/bin/bash
DOCKERHOSTIP=$(ip addr | awk '/inet/ && /docker0/{sub(/\/.*$/,"",$2); print $2}')
TEST_TARGET='http://'$DOCKERHOSTIP':8080/people'
docker build -t locust-test:latest .
docker run --rm -p 8089:8089 -e LOCUST_MODE=standalone -e TARGET_URL=$TEST_TARGET locust-test
echo 'open browser at http://localhost:8089'

```

## Access locust
open http://localhost:8089 in a browser.
