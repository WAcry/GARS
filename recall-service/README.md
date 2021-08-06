# Recall Service for GARS

## Setup

- Make sure Python 3.8 & virtualenv is installed first
- `virtualenv venv --python=python3`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- Set correct path of dataset and ports in /recall/config.py
## Run

- `source venv/bin/activate`
- `./start.sh`

## API

- `GET` `/?user_id=<uid>`
    - Get recall for a user
    - Returns list of anime ids

- `GET` `/sim?anime_id=<aid>`
    - Get similar items for an anime
    - Returns list of anime ids

Check examples in /test dir

## Train Embedding Model

- setup redis (docker is the easiest way) and run redis-server first
- setup correct config in /recall/config.py
- `source venv/bin/activate`
- `./train.sh`


