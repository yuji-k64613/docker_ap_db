#!/bin/bash
cat /tmp/sql.txt | PGPASSWORD=password psql --dbname=postgres --user=postgres
