from random import randint
import json

LETTER_RANGE = [97, 122]

def rando(range):
  return randint(range[0], range[1])

def make_word(num_letters, capital=False):
  result = ''
  for i in range(num_letters):
    letter = chr(rando(LETTER_RANGE))
    if capital and i == 0:
      letter = letter.upper()
    result += letter
  return result

def make_sentence(num_words, word_length_range):
  result = ''
  for i in range(num_words):
    result += make_word(rando(word_length_range), i == 0)
    result += ' '
  result = result[:-1]
  result += '.'
  return result

def make_paragraph(num_sentences, sentence_length_range, word_length_range):
  result = ''
  for i in range(num_sentences):
    result += make_sentence(rando(sentence_length_range), word_length_range)
    result += ' '
  result = result[:-1]
  return result

def make_story(num_paragraphs, paragraph_length_range, sentence_length_range, word_length_range):
  result = ''
  for i in range(num_paragraphs):
    result += make_paragraph(rando(paragraph_length_range), sentence_length_range, word_length_range)
    if i != num_paragraphs - 1:
      result += '\n\t'
  return result

# just hardcoding values here
def make_entry():
  result = {}
  result['author'] = make_word(randint(3, 10), True) + ' ' + make_word(randint(5, 10), True)
  result['title'] = make_sentence(randint(3, 10), [3, 12])
  result['date'] = randint(1, 10000)
  result['story'] = make_story(5, [3, 20], [5, 10], [5, 10])
  return result

data = []
for i in range(10):
  data.append(make_entry())

with open("output.json", "w") as outfile:
  outfile.write(json.dumps(data))
