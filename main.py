long_string = 'this is a loooooooooong string'

# walrus operator assins len(x) to n
if ((n := len(long_string)) > 16):
  print(f"This string has a length of {n}")

a = 'hellooooooooooooooooooo'
while ((n := len(a)) > 5):
  print(n)
  a = a[:-1]
print(a[:])
  
  
