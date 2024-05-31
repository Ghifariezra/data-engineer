# How is work ?
1. First, you can build and run a hadoop container
```
docker-compose -f docker-hadoop/docker-compose-hadoop.yml up -d
```

2. Then, you can make directory hdfs
```
docker exec docker-hadoop-namenode-1 \
bash -c \
"hadoop fs -mkdir /data-poke"
```

3. And last, you can paste all data that from local system `/scripts/data/*` to hdfs
```
docker exec docker-hadoop-namenode-1 \
bash -c \
"hadoop fs -put /scripts/data/*.csv /data-poke"
```

4. And you can check data in hdfs
```
docker exec docker-hadoop-namenode-1 \
bash -c \
"hadoop fs -ls /data-poke"
```

5. If you want to delete all data in hdfs
```
docker exec docker-hadoop-namenode-1 \
bash -c \
"hadoop fs -rm -f -r /data-poke"
```