import json
from flask import request, Flask
from flask.helpers import make_response
from flask_restful import Resource, Api
from japanese_tokenizer import JapaneseTokenizer

STATUS_UNPROCESSABLE_ENTITY = 422

app = Flask(__name__)
api = Api(app)
japanese_tokenizer = JapaneseTokenizer()

# Use this to avoid responses that contain texts like "\u53ef\u611b\u3044".
@api.representation('application/json')
def output_json(data, code, headers):
  resp = make_response(json.dumps(data, ensure_ascii=False), code)
  resp.headers.extend(headers)
  return resp

class TokenizeResource(Resource):
  def post(self):
    text = request.json.get('text')
    if text is None:
      return { 'error': "'text' key missing in JSON" }, STATUS_UNPROCESSABLE_ENTITY
    return { 'result': japanese_tokenizer.extract_word_list(text) }

api.add_resource(TokenizeResource, '/tokenize')

if __name__ == '__main__':
  app.run(debug=True)
