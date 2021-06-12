# API-Service

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
    - Get anime recommends for a user


- `GET` `/sim?anime_id=<aid>`
    - Get similar animes for a given one

Check examples in /test dir