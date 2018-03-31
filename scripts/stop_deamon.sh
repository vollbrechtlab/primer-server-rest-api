#!/bin/bash
pids=`ps ax | grep primer-server-rest-api-deamon-v1.0.4 | cut -c2-5`
pid=${pids:0:4}
echo "killing ${pid}"
kill $pid
