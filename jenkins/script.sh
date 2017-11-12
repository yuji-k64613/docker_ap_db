#!/bin/bash
export JAVA_HOME=$(readlink /etc/alternatives/java | sed 's:/bin/java$::')
java -jar jenkins.war
