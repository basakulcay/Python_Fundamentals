def count_char_x(word,x):
  counter=0
  for w in word:
    if x in w:
      counter+=1
    else:
      counter+=0
  return counter


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
