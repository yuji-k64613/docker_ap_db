http://localhost:9090/

#cat /root/.jenkins/secrets/initialAdminPassword
docker-compose exec jenkins cat /root/.jenkins/secrets/initialAdminPassword

#mv /tmp/sample01 /root/.jenkins/jobs
#mv /tmp/sample02 /root/.jenkins/jobs
cd ansible
ansible-playbook jenkins_init.yml
