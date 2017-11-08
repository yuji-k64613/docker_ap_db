FROM centos

RUN yum update -y
RUN yum install -y \
  curl \
  java \
  unzip

COPY wlp-javaee7-17.0.0.2.zip /opt
WORKDIR /opt
RUN unzip wlp-javaee7-17.0.0.2.zip

WORKDIR /opt/wlp
RUN ./bin/server create server1
RUN sed -i '/<\/server>/i<keyStore id="defaultKeyStore" password="password"/>' ./usr/servers/server1/server.xml
RUN sed -i '/<httpEndpoint/ahost="*"' ./usr/servers/server1/server.xml

COPY datasource.txt /tmp
RUN sed -i '/<server/r /tmp/datasource.txt' ./usr/servers/server1/server.xml

COPY postgresql-42.1.1.jar /opt
COPY mariadb-java-client-2.1.2.jar /opt

COPY myapp.war ./usr/servers/server1/dropins/

CMD ./bin/server run server1
