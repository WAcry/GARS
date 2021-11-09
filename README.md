# Great Anime Recommendation System

This project implements a recommendation system for anime using modern machine learning techniques.

## Tech Stacks

**Python 3, Flask, Spark, Kafka, Flink, Redis, Tensorflow Keras, Docker, Vue.js, Scrapy, Cassandra**

## Features

- Given a user, return a list of anime recommendations.
- Given a user, return a list of similar users.
- Given an anime, return a list of similar anime.
- **React in real-time** based on user's click actions and adjust the recommendation list accordingly.

## Benchmark

Trained model used in rank-service has about **80% accuracy** on the test-dataset 
predicting if a user will like an anime (rating > 7).

## Project Structure

- `dataset`: dataset used in the recommendation system
- `web-service`: frontend of the recommendation system
- `api-service`: backend controller of the recommendation system
- `recall-service`: the first filter of the recommendation system
- `rank-service`: the second filter of the recommendation system
- `kafka-service`: monitor user's click actions and send to Kafka
- `flink-service`: consume user's click actions from Kafka and update new feature data in redis

## Demo Images

![](https://raw.githubusercontent.com/Quakiq/tinyimages/main/img202206260702367.png)

-----

![](https://raw.githubusercontent.com/Quakiq/tinyimages/main/img202206260710947.png)

## Details & Deployment

### Recall Service

This microservice is the first filter of the recommendation system.
It is responsible for return a **large** list of anime recommendations from the original very large dataset.
Because the original dataset is too large, it needs to use simple and fast strategies.

The most important strategy here is the **Item2Vec** Model, works with **locality sensitive hashing** algorithm that finds close user embedding and anime embedding.
The model input is generated based on **Deep Walk** algorithm and **Min-Max Scaler**, and the output is stored in **Redis**.


#### Setup

First, make sure Python 3.8 & virtualenv is installed first

```
virtualenv venv --python=python3
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

Set correct path of dataset and ports in `/recall/config.py`, `start.sh`, and `train.sh`

Setup redis (docker is the easiest way) and run redis-server first 

Setup correct config in /recall/config.py

```
source venv/bin/activate
```

run `./train.sh` to generate the word2vec model and store it in redis

#### Run

```
source venv/bin/activate
```
```
./start.sh
```

#### API

- `GET` `/?user_id=<uid>`
    - Get recall for a user
    - Returns list of anime ids

- `GET` `/sim?anime_id=<aid>`
    - Get similar items for an anime
    - Returns list of anime ids

**Check examples in /test dir**


### Rank Service

This microservice is the second filter of the recommendation system.
It is responsible for return a **small** list of anime recommendations based on returns from recall service.

**Collaborative filtering** algorithm is implemented here to generate recommendations. While, MLP model shows a better performance and replace collaborative filtering algorithm.

**Tensorflow** is used to train a MLP model to predict user's like animes, based on user features (top preferred tags, avg rating, etc)
and anime features (tags, release date, etc). **Hparams** and **Tensorboard** are used to monitor the training process and find the best hyperparameters of MLP. The model has **80% accuracy** on the test-dataset predicting if a user will like an anime (rating > 7).

**End to end embedding** strategy is used to for categorical features. Here's how the model looks like:
![](https://raw.githubusercontent.com/Quakiq/tinyimages/main/img202206260822843.png)

#### Setup

First, make sure Python 3.8 & virtualenv is installed first

```
virtualenv venv --python=python3
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

Set correct info (such as port and data directory) in `rank/config.py` and `start.sh`

Make sure Redis is running (install and start redis and redis-server, don't forget to close the firewall)
Run Feat Eng.ipynb to store initial newest feature data in redis
MLP Model is trained already by MLP.ipynb, so no need to train again

#### Run

```
source venv/bin/activate
```
```
./start.sh
```

#### API

- `GET` `/?user_id=<uid>`
    - Get rank results for a user
    - Returns list of anime ids

**Check examples in /test dir**

### Kafka Service

This microservice monitors user's click actions and send to Kafka in **real-time**.

#### Setup

First, make sure Python 3.8 & virtualenv is installed first

```
virtualenv venv --python=python3
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

#### Install Kafka with Zookeeper

need to set up kafka and zookeeper, [kafka-docker](https://github.com/WAcry/kafka-docker) is one of good options:

```
docker-compose up -d

docker ps # to check if everything is ok (should have 2 containers running for kafka and zookeeper)
```

#### Run
```
flask run
```

#### API

- `POST` `/clicks`
  ```
  {
    user_id: <uid>, 
    anime_id: <aid>
  }
  ```
  - Get rank results for a user

  - Returns list of anime ids

**Check examples in /test dir**

### Flink Service

This microservice uses Flink to get new clicks from kafka and write new features to redis in **real-time**.

#### Setup

First, make sure Python 3.8 & virtualenv is installed first

```
virtualenv venv --python=python3
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```


Copy `flink-sql-connector-kafka-1.15.0.jar` to `venv/lib/python3.8/site-packages/pyflink/lib`

#### Run

```
source venv/bin/activate
```
```
./start.sh
```

### API Service

This microservice is the backend controller for GARS

#### Setup

First, make sure Python 3.8 & virtualenv is installed first

```
virtualenv venv --python=python3
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

Set correct path of dataset and ports in /recall/config.py and start.sh

#### Run

```
source venv/bin/activate
```
```
./start.sh
```

#### API

- `GET` `/?user_id=<uid>`
    - Get anime recommends for a user


- `GET` `/sim?anime_id=<aid>`
    - Get similar animes for a given one

**Check examples in /test dir**

### Web Service

This microservice is the frontend of the recommendation system.

#### Setup

```
npm install
```

#### Run

```
npm run serve
```


### Dataset & Spider

The dataset used in this project is collected from [MyAnimeList](https://myanimelist.net/). It contains 
each user's rating on different animes, and also all information about each anime.

A Scrapy spider is written to collect the data. You can find it in the `/dataset/animelist` directory.

run command `scrapy crawl anime -o output.csv -t csv` to start the spider. Make sure the spider is not running too 
fast, otherwise you may be banned from scraping.

`anime.csv` `rating.csv` are original dataset

`merged.csv` are left join of original dataset and crawler data for more info about each anime

`parsed_anime.csv` reformat dates in merged.csv

`animelist` directory contains a scrapy spider that scrapes anime data from animelist.net

