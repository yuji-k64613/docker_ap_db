#!/bin/bash
# 起動
/opt/wildfly/bin//standalone.sh &

# 起動待ち
sleep 3
RET=1
while [ $RET != 0 ]
do
	/opt/wildfly/bin/jboss-cli.sh --connect ls
	RET=$?
	sleep 3
done

# ユーザ作成
/opt/wildfly/bin/add-user.sh -u admin -p password
# データソース作成
cat /tmp/jboss-cli.txt | /opt/wildfly/bin/jboss-cli.sh
# デプロイ
/opt/wildfly/bin/jboss-cli.sh --connect 'deploy /tmp/myapp.war'

# exit対策
tail -f /dev/null
