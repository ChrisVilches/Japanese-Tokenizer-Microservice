# Japanese Tokenizer Microservice

A microservice that makes it easy to tokenize Japanese texts. Useful for making word clouds, analyzing texts, or getting the most important words from a sentence.

It uses Flask (lightweight Python web framework), and MeCab for text segmentation.

TODO: Use a better example (longer text from Wikipedia or something).

```
PUT /important_words
{
  "text": "説明書の例文を付けてください。"
}
```

Returns:

```json
{
  "result": ["説明", "書", "例文", "付ける", "くださる"]
}
```

## Installation

Requires Python 3 (created using 3.8.10) and `pip3`.

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Install mecab.

Test mecab by executing this command:

```bash
echo "辞書" | mecab
```

And the result should be:

```bash
辞書    名詞,一般,*,*,*,*,辞書,ジショ,ジショ
EOS
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
curl -X POST http://localhost:45678/important_words -d "{\"text\": \"猫が可愛かった\"}" -H "Content-Type: application/json"
```

Result should be:

```json
{
  "result": ["猫", "可愛い"]
}
```
