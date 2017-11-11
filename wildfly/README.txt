http://localhost:8080/myapp/service/main/foo?id=1
http://localhost:9990
#admin/password

修正:src/main/resources/META-INF/persistence.xml
<jta-data-source>java:jboss/datasources/MariaDS</jta-data-source>
<jta-data-source>java:jboss/datasources/PostgresDS</jta-data-source>
