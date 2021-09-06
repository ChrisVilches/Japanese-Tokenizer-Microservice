import os
import re

class Util:
  @staticmethod
  def clean_text(text):
    return re.sub(r':[a-zA-Z_-]+:', '', text)

  @staticmethod
  def file_lines_to_set(relative_filename):
    absolute_path = os.path.join(os.getcwd(), relative_filename)
    lines = open(absolute_path, encoding='UTF-8').read().split('\n')
    lines = list(filter(None, lines)) # Remove empty lines.
    return set(lines)
