def every_other_letter(word):
  new_word = ""
  for i in range(0, len(word), 2):
    new_word += word[i]
  return new_word
    


def every_other_letter(word):
  new_word = ''
  counter = 0
  for letter in word:
    if counter % 2 == 0:
      new_word += letter
    counter += 1
  return new_word


def every_other_letter(word):
    return word[::2]

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))



