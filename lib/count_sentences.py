#!/usr/bin/env python3

class MyString:
  def __init__(self, value = None):
    self._value = None
    self.value = value

  @property

  def value (self):
    return self._value
  
  @value.setter

  def value (self, new_value):
    if isinstance(new_value, str):
      self._value = new_value

  def is_sentence (self):
    if self._value is not None:
      return self._value.endswith('.')
    return False
  
  def is_question(self):
    if self._value is not None:
      return self._value.endswith('?')
    return False
  
  def is_exclamation(self):
    if self._value is not None:
      return self._value.endswith("?")
    return False
  
  def count_sentences (self):
    if self._value is not None:
      sentences = [sentences.strip() for sentence in re.split(r'[.!?]', self._value) if sentence]
      return len(sentences)
    return 0

  pass
