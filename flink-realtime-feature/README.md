# Flink
Use Flink to get new clicks from kafka and write new features to redis

## SETUP

- `virtualenv venv --python=python3`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- Copy flink-sql-connector-kafka-1.15.0.jar to venv/lib/python3.8/site-packages/pyflink/lib

## RUN

- `source venv/bin/activate`
- `python ./flink-kafka.py` or `python flink-kafka.py`

