#!/bin/bash

cd src
ls
service openvswitch-switch start
mn -c
rm ./logs/*

screen -dmSL main python3 topo.py
tail -f /dev/null