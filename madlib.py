import re

print('Welcome to Madlibs. Please follow the prompts to get a fun lil madlib')

# User prompt
adj_one = input('I need an adjective')
adj_two = input('I need an adjective')
noun_one = input('I need a noun')

#declaring regex to find inputs
regex = r"(?<={).*?(?=})"

# File manipulation
with open ('assets/dark_and_story_night_template.txt') as file:
  unparsed_message = file.read().strip()
  print(unparsed_message)


speech_parts = re.findall(regex, unparsed_message)
print(speech_parts)

parsed_message = re.sub(regex,'', unparsed_message)
print(parsed_message)

filled_message =  parsed_message.format(adj_one, adj_two, noun_one)
print(filled_message)
