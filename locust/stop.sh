#!/bin/bash
docker stop $(docker ps -q --filter ancestor=locust-test)
docker rm $(docker ps -q -a --filter ancestor=locust-test)
