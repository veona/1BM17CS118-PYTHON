class admit():
  def __init__(self):
   self.__studentid__=None
   self.__age__=None
   self.__marks__=None
  def validate_age(self):
   if self.__age__>20:
    return True
   else:
    return False
  def validate_marks(self):
    if self.__age__ in range(1,101):
     return True
    else:
     return False
  def check_qualification(self):
   if self.validate_age() and self.validate_marks():
     if self.__marks__>60:
      return True
     else:
      return False
   else:
    return False
  def setter_method(self):
   self.__studentid__=input('enter student id')
   self.__age__=int(input('enter age'))
   self.__marks__=int(input('enter marks'))
  def getter_method(self):
   print('STUD_ID',self.__studentid__)
   print('age:',self.__age__)
   print('marks:',self.__marks__)
   if self.check_qualification():
    print('qualified')
   else:
    print('not eligible')
s1=admit()
s1.setter_method()
s1.getter_method()
    
