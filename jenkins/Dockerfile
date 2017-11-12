FROM centos

RUN yum update -y
RUN yum install -y \
  curl \
  git \
  java \
  maven \
  unzip

RUN mkdir -p /opt/jenkins
COPY jenkins.war /opt/jenkins
ADD sample01 /tmp/sample01
ADD sample02 /tmp/sample02
ADD script.sh /opt/jenkins

WORKDIR /opt/jenkins
CMD ./script.sh
