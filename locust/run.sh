#!/bin/bash

docker build -t locust-test:latest .
docker run --rm -p 8089:8089 -e LOCUST_MODE=standalone -e TARGET_URL=http://127.0.0.1 locust-test
echo 'open browser at http://localhost:8089'
