# Rank Service

## Setup

- Make sure Python 3.8 & virtualenv is installed first
- `virtualenv venv --python=python3`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- Set correct info (such as port and data directory) in `config.py` and `start.sh`

- Make sure Redis is running (install and start redis and redis-server)
- Run Feat Eng.ipynb to store initial newest feature data in redis
- Model is trained already by MLP.ipynb, so no need to train again

## Run

- `source venv/bin/activate`
- `./start.sh`

## API

- `GET` `/?user_id=<uid>`
    - Get rank results for a user
    - Returns list of anime ids

Check examples in /test dir