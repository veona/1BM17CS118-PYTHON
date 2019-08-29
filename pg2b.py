s=input('enter string')
l=s.split()
l.reverse()
for i in l:
  print(i,end=' ')
l.reverse()
for i in l:
  print(i[-1::-1],end=' ')
