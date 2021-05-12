# Write your x_length_words function here:
def x_length_words(sentence,x):
  word=sentence.split(" ")
  lengths=[]
  for w in word:
    length=len(w)
    lengths.append(length)

  counter=0
  for i in lengths:
    if i>=x:
      counter+=1
  if counter==len(word):
    return True
  else:
    return False
  
  #if length>=x:
   # return True
  #else:
   # return False
 
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
