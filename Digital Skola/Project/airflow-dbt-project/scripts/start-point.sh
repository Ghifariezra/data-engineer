#!/bin/bash

SPARK_WORKLOAD=$1

echo "SPARK_WORKLOAD: $SPARK_WORKLOAD"

if [ "$SPARK_WORKLOAD" == "master" ];
then
  start-master.sh -p $SPARK_PORT
elif [ "$SPARK_WORKLOAD" == "worker" ];
then
  start-worker.sh spark://$SPARK_MASTER:$SPARK_PORT
fi