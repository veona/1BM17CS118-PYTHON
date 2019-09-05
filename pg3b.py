import random
import string
def fun():
 letters=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
 length=random.randint(8,12)
 return ' '.join(random.sample(letters,length))
flag=1
while flag:
  print('press 1 to get password & 2 to exit')
  p=int(input())
  if p==1: 
    print(fun())
  else:
    flag==0
