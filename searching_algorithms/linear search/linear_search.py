# details of the logic behind the algorithm are in the README file, but it is really simple to understand
def linear_search(array, length_array, chosen_element):
  for i in range(0, length_array): # going through every index
    
    #seeing if it's a match
    if(array[i] == chosen_element):
      return i
  return -1 # if not will return -1
  
  
array = [200, 500, 4, -3, 8]
length_array = len(array)
chosen_element = 500
result_search = linear_search(array, length_array, chosen_element)

if(result_search == -1):
  print("This element is not present in the array in question")
else:
  print("The element is present at index: ", result_search)
