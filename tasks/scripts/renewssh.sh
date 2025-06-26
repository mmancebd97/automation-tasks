#!/bin/bash

#promp for variable
read -p "ip para renovar:" IP

#vars
CONT="d87bf4ae3a29"
COMAN="ssh-keygen -R $IP" 

#execute in container
docker exec  "$CONT"  $COMAN
