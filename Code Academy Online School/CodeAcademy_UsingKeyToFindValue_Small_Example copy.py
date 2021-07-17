"" This one was if the key (int) was divisible by 2 or even.Then increase the sum
return the even keys count """

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
""" if key even in dict then count plus one , return sum of even keys """
  list1 = []
  count = 0
  sum = 0
  for key in my_dictionary.keys():
    list1.append(my_dictionary[key])
    if int(key) % 2 == 0:
      sum += list1[count]
    count += 1
  return sum
print(sum_even_keys({1:2,2:0,2:3,8:99}))
# Uncomment these function calls to test your  function:
#print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
#print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6