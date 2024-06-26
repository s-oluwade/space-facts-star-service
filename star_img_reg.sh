#!/bin/bash

docker tag star-facts-service:latest 533266979424.dkr.ecr.us-east-1.amazonaws.com/star-facts-service:latest
docker push 533266979424.dkr.ecr.us-east-1.amazonaws.com/star-facts-service:latest
