""" To write the first letter of the last name... then the number of first names in dict for as in S:3 for {Stark:[cody,ned,elmo]} 
"""
# Write your count_first_letter function here:
def count_first_letter(names):
""" return the first letter of the last name (key) and the number of first names it has. so Smith,Smithy,Smith,Sammers S:4...Kawasaki K:1 """
  dictionary = {}
  for keys in names.keys():
    dictionary.update({keys[0]:0})
  for k,v in names.items():
    count = 0
    for sub_val in v:
      count += 1
    dictionary[k[0]] += count
  return (dictionary)
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
    

# Uncomment these function calls to test your  function:
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}