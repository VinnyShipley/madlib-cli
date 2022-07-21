import re

print('Welcome to Madlibs. Please follow the prompts to get a fun lil madlib')

# User prompt
adj_one = input('I need an adjective ')
adj_two = input('I need an adjective ')
noun_one = input('I need a noun ')

input_tuple = (adj_one, adj_two, noun_one)

print(input_tuple)

#declaring regex to find inputs
regex = r"(?<={).*?(?=})"

# File manipulation
with open ('assets/dark_and_story_night_template.txt') as file:
  

  read_template = file.read().strip()
print(read_template + 'read template')


speech_parts = re.findall(regex, read_template)
print(speech_parts)

parsed_message = re.sub(regex,'', read_template)
print(parsed_message + 'parsed message')

filled_message =  parsed_message.format(adj_one, adj_two, noun_one)
print(filled_message + 'filled message')

def merge(b, **a):
  print(a)
  print(b)
  new_sentence = a.format(b)
  return new_sentence



print(merge(parsed_message, input_tuple) + 'merged')
