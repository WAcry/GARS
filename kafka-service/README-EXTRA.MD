## Init

- `virtualenv venv --python=python3`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## Kafka with Zookeeper

set up kafka and zookeeper, docker is one of good options:

https://github.com/WAcry/kafka-docker

docker-compose up -d

docker ps # to check if everything is ok (should have 2 containers running for kafka and zookeeper)

## Run

`flask run` to start app.py simply

## BELOW IS JUST FOR CONSUMER DEMO, WHICH IS NOT REQUIRED FOR THIS PROJECT TO WORK

## Init Cassandra
```
CREATE KEYSPACE actions WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
create table views (user_id int,anime_id int,happened_at timestamp,primary key (user_id, anime_id, happened_at));
create table clicks (user_id int,anime_id int,happened_at timestamp,primary key (user_id, anime_id, happened_at));
```

## start
edit start-consumer.sh to change mode (view or click) and topic name
use start-consumer.sh to start kafka consumer
request to app.py and view/click will be sent to kafka then stored in cassandra

