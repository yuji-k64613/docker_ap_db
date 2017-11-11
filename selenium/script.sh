#!/bin/bash
export DISPLAY=:1
vncserver $DISPLAY -geometry 1024x768
fvwm &

PATH=$PATH:.
cd /root
java -jar selenium-server-standalone-3.6.0.jar &

tail -f /dev/null
