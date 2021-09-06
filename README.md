# Japanese Tokenizer Microservice

A microservice that makes it easy to tokenize Japanese texts. Useful for making word clouds, analyzing texts, or getting the most important words from a sentence.

It uses Flask (lightweight Python web framework), and MeCab for text segmentation.

TODO: Use a better example (longer text from Wikipedia or something).

```
PUT /important_words
{
  "text": "プログラミング言語は、その開発の背景や機能などの影響を受け、言語によって得意とする分野は異なります。"
}
```

Returns:

```json
{
  "result": [
    "プログラミング", "言語", "開発", "背景",
    "機能", "影響", "受ける", "言語", "得意",
    "する", "分野", "異なる"
  ]
}
```

## Installation

Requires Python 3 (created using 3.8.10) and `pip3`.

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Install mecab and dictionaries. There are many ways, but here's one that can help: https://qiita.com/ekzemplaro/items/c98c7f6698f130b55d53

Test mecab by executing this command:

```bash
echo "辞書" | mecab
```

And the result should be:

```bash
辞書    名詞,一般,*,*,*,*,辞書,ジショ,ジショ
EOS
```

## Run app

```bash
export FLASK_APP=server.py
export FLASK_RUN_PORT=45678 # Your desired port.
export FLASK_ENV=development
flask run
```

And test using:

```bash
curl -X POST http://localhost:45678/important_words -d "{\"text\": \"猫が可愛かった\"}" -H "Content-Type: application/json"
```

Result should be:

```json
{
  "result": ["猫", "可愛い"]
}
```

## Possible Errors

### Cannot find mecab path

Sometimes the app fails because it doesn't find mecab. Find and set it using:

```bash
# Returns its path, in my case /etc/mecabrc
sudo find / -iname mecabrc

# Set environment variable.
export MECABRC='/etc/mecabrc'

# Run app.
flask run
```
