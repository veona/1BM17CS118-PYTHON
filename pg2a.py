l=list(map(int,input('enter the list').split()))
n=int(input('enter no to be searched'))
def fun(l,num):
  if num in l:
    return True
  else:
    return False
print(fun(l,n))
