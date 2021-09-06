class Word:
  # These are indices in this array:
  # ['名詞', '一般', '*', '*', '*', '*', '猫', 'ネコ', 'ネコ']
  WORD_TYPE_INDEX = 0
  FULL_WORD_INDEX = 6
  READING_INDEX = 7

  word = None
  word_type = None
  reading = None

  @staticmethod
  def from_part_of_speech_array(array):
    word = Word()
    word.word = array[Word.FULL_WORD_INDEX] # Used to be node.surface, but there's no documentation about what it does.

    if word.word == '*':
      return None

    word.word_type = array[Word.WORD_TYPE_INDEX]
    word.reading = array[Word.READING_INDEX]
    return word
