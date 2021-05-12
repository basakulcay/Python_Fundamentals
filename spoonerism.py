# Write your make_spoonerism function here:
def make_spoonerism(word1,word2):
  fs1=word1[0]
  fs2=word2[0]

  new1=fs2+word1[1:]
  new2=fs1+word2[1:]

  return new1+" "+new2
  
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
