#!/bin/bash
cat /tmp/root.txt | mysql -uroot -ppassword
cat /tmp/user.txt | mysql -umariadb -ppassword
