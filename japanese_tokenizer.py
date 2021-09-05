import MeCab # TODO: I don't have any dictionary file in here, where is the file configured at?
import re

class JapaneseTokenizer:
  # These are indices in this array:
  # ['名詞', '一般', '*', '*', '*', '*', '猫', 'ネコ', 'ネコ']
  WORD_TYPE_INDEX = 0
  FULL_WORD_INDEX = 6

  # TODO: Make at least stop words configurable from a file.

  STOP_WORDS = set({
    'こと',
    'よう',
    'ん',
    'の',
    'は'
  })

  ALLOWED_TYPES = set([
    '名詞',
    '副詞',
    '形容詞'#, '連体詞', '感動詞'
  ])

  tagger = None

  def __init__(self):
    print("Creating new tokenizer object.")
    self.tagger = MeCab.Tagger()
    self.tagger.parse('')

  def clean_text(self, text):
    return re.sub(r':[a-zA-Z_-]+:', '', text)

  def extract_word_list(self, text):
    text = self.clean_text(text)
    node = self.tagger.parseToNode(text)
    word_list = []
    while node:
      parts = node.feature.split(',')
      word_type = parts[self.WORD_TYPE_INDEX]
      word = parts[self.FULL_WORD_INDEX] # Used to be node.surface, but there's no documentation about what it does.
      node = node.next

      if word in self.STOP_WORDS:
        continue
      if word_type in self.ALLOWED_TYPES:
        word_list.append(word)
    return word_list
