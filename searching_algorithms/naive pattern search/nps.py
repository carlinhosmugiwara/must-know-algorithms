  
# Naive pattern searching algorithm, details about the logic behind the algorithm are in the README.md file


def nps(string, pattern):
  x = len(string) # length of the whole string
  y = len(pattern) # length of the substring
  
  if(y<x): # make sure that y is less than x because we're talking about a substring here
    for i in range(x - y + 1): # the logic behind this number is in this case, we start searching the indexes "0123" and then "1234" and so "2345".... 
      j = 0
      
      #checking for the actual match
      while(j<y):
        if(string[i + j] != pattern[j]:
          break
        j+=1
      if(j == y):
        print("The pattern in question was found at index: ", i)

# now the testing
string = "xxyabgdxxyzkp"
pattern = "xxyz"
nps(string, pattern)
