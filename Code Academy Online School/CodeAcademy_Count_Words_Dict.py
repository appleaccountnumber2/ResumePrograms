""" This exercise was to return a list of words inputted with a count for how many letters
in each word, believe it or not they didn't want (4 letters: 2 words) instead just to return
the word itself with how many letters in each one (so duplicate words) """

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
""" return a list of words and a count of letters in that word. as in cat : 3 """
  dictionary = {}
  for word in words:
    dictionary.update({word:len(word)})
  return dictionary
print(word_length_dictionary(['test','ball','water','fountain','sack','pen','night','night','lemon','lime','time','obama']))
# Uncomment these function calls to test your  function:
#print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
#print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}