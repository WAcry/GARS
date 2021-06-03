# Rank Service

## Setup

- Make sure Python 3.8 & virtualenv is installed first
- (Optional)`virtualenv venv --python=python3`
- (Optional)`source venv/bin/activate`
- `pip install -r requirements.txt`
- Set correct ports in ./start.sh

## Run

- `source venv/bin/activate`
- `./start.sh`

## API

- `GET` `/?user_id=<uid>`
    - Get rank results for a user
    - Returns list of anime ids

Check examples in /test dir