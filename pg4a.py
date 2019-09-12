class admit():
  def __init__(self):
   self.__studentid=None
   self.__age=None
   self.__marks=None
  def validate_age(self):
   if self.__age>20:
    return True
   else:
    return False
  def validate_marks(self):
    if self.__age in range(1,101):
     return True
    else:
     return False
  def check_qualification(self):
   if self.validate_age() and self.validate_marks():
     if self.__marks>60:
      return True
     else:
      return False
   else:
    return False
  def setter_method(self):
   self.__studentid_=input('enter student id')
   self.__age=int(input('enter age'))
   self.__marks=int(input('enter marks'))
  def getter_method(self):
   print('STUD_ID',self.__studentid)
   print('age:',self.__age)
   print('marks:',self.__marks)
   if self.check_qualification():
    print('qualified')
   else:
    print('not eligible')
'''s1=admit()
s1.setter_method()
s1.getter_method()'''
n=int (input('enter no'))
stlist=[admit() for j in range(n)]
for i in range(n):
  stlist[i].setter_method()
for i in range(n):
  stlist[i].getter_method()
    
