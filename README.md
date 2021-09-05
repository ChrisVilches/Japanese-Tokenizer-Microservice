# Japanese Tokenizer Microservice

TODO: Put here a sample of what it does.

## Installation

Requires Python 3 (created using 3.8.10) and `pip3`.

Install dependencies:

```bash
pip3 install -r requirements.txt
```

TODO: Explanation related to dictionary files (but I want to include them in the repository, so
      that it's not necessary to explain how to do anything).

## Run app

```bash
export FLASK_APP=server.py
export FLASK_RUN_PORT=45678 # Your desired port.
export FLASK_ENV=development
flask run
```

And test using:

```bash
curl -X POST http://localhost:45678/tokenize -d "{\"text\": \"猫が可愛い\"}" -H "Content-Type: application/json"
```

Result should be:

```json
{
  "result": ["猫", "可愛い"]
}
```
