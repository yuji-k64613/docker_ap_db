#!/bin/bash
export DISPLAY=:1
fvwm &
vncserver :1 -geometry 1024x768
PATH=$PATH:.
cd /root
java -jar selenium-server-standalone-3.6.0.jar &
tail -f /dev/null
