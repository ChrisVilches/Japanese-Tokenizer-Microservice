import MeCab
from word import Word
from util import Util

class JapaneseTokenizer:
  STOP_WORDS_CONFIG_FILE = 'config/stop_words.txt'
  ALLOWED_TYPES_CONFIG_FILE = 'config/allowed_types.txt'

  stop_words = set([])
  allowed_types = set([])

  tagger = None

  def __init__(self):
    print("Creating new tokenizer object.")
    self.tagger = MeCab.Tagger()
    self.tagger.parse('')
    self.read_stop_words()
    self.read_allowed_types()

  def read_stop_words(self):
    self.stop_words = Util.file_lines_to_set(self.STOP_WORDS_CONFIG_FILE)
    print('Stop words:')
    print(self.stop_words)

  def read_allowed_types(self):
    self.allowed_types = Util.file_lines_to_set(self.ALLOWED_TYPES_CONFIG_FILE)
    print('Allowed types:')
    print(self.allowed_types)

  def should_add_word(self, word):
    if word is None or word.word in self.stop_words:
      return False

    return word.word_type in self.allowed_types

  def text_to_word_list(self, text):
    text = Util.clean_text(text)
    node = self.tagger.parseToNode(text)
    word_list = []
    while node:
      parts = node.feature.split(',')
      word = Word.from_part_of_speech_array(parts)
      node = node.next

      if self.should_add_word(word):
        word_list.append(word)
    return word_list

  def extract_word_list_only_word(self, text):
    result_list = []
    for w in self.text_to_word_list(text):
      result_list.append(w.word)
    return result_list

  def extract_word_list_metadata(self, text):
    result_list = []
    for w in  self.text_to_word_list(text):
      result_list.append({
        'word': w.word,
        'type': w.word_type,
        'reading': w.reading
      })
    return result_list
