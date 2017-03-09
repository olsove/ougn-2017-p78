#!/bin/bash
DOCKERHOSTIP=$(ip addr | awk '/inet/ && /docker0/{sub(/\/.*$/,"",$2); print $2}')
TEST_TARGET='http://'$DOCKERHOSTIP':8080/people'
docker build -t locust-test:latest .
docker run --rm -p 8089:8089 -e LOCUST_MODE=standalone -e TARGET_URL=$TEST_TARGET locust-test
echo 'open browser at http://localhost:8089'
