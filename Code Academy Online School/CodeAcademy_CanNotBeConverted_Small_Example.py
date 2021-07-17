"" This exercise was summing all the values of the dictionary keys
,added except the one that can't be converted (a float) to an int for summing"""

# Write your sum_values function here:
def sum_values(my_dictionary):
""" sum all of the key's values except what can't be converted to an int I chose float to not be summed"""  
  value_sum = 0
  for value in my_dictionary.values():
    if type(value) is int:
      value_sum += int(value)
    elif type(value) is not int:
      try:
        a = int(value)
        if type(a) is int:
          value_sum += int(value)
      except:
        print('This val cannot be converted to an interger',value)
      continue
  return value_sum
print(sum_values({'mile':5000,'cody':2,'foot':1,'football':'1.4'}))
# Uncomment these function calls to test your sum_values function:
#print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
#print(sum_values({10:1, 100:2, 1000:3}))
# should print 6