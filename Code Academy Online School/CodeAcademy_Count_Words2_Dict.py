""" Exercise codecademy #4 ...Just updating a word count in a dictionary """


"""This was done so one may see a programmers simple solutions to problems, and how code looks"""

""" Putting a three quote definition for every function and every class is standard """


# Write your frequency_dictionary function here:
def frequency_dictionary(words):
""" count frequency of words return dict """
  a = 0
  dictionary = {}
  count = 0
  for word in words:
        if word in dictionary.keys():
          for key in dictionary.keys():
            if key == word:
              dictionary[key] += 1
        else:
          dictionary.update({word:1})


  return dictionary
print(frequency_dictionary(['cody','body','floatie','cody','nigeria','africa','iceland']))
# Uncomment these function calls to test your  function:
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}