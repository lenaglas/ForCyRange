#!/bin/bash

pkill screen
docker-compose up
screen -dmSL api python3 api.py