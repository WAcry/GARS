## Init

install requirements as other packages

## Init Cassandra

```
CREATE KEYSPACE actions WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
create table views (user_id int,anime_id int,happened_at timestamp,primary key (user_id, anime_id, happened_at));
create table clicks (user_id int,anime_id int,happened_at timestamp,primary key (user_id, anime_id, happened_at));
```

## Kafka with Zookeeper

set up kafka and zookeeper, docker is one of good options:

https://github.com/WAcry/kafka-docker

docker-compose up -d

docker ps # to check if everything is ok (should have 2 containers running for kafka and zookeeper)



