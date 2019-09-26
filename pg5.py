class CallDetail:
     def _init_(self):
        self.calling_num=None
        self.called_num=None
        self.duration=None
        self.type=None
class Util:
     def __init__(self):
        self.list_of_call_objects=[]
        self.std=0
        self.isd=0
        self.local=0
     def parse_customer(self,list_of_call_string):
         for i in range(len(list_of_call_string)): 
           obj=CallDetail()
           l=list_of_call_string[i].split(',')
           obj.calling_num=l[0]
           obj.called_num=l[1]
           obj.duration=l[2]
           obj.type=l[3]
           self.list_of_call_objects.append(obj)
     def display(self):
       for i in range(len(self.list_of_call_objects)):
         print('caling no:',self.list_of_call_objects[i].calling_num)
         print('called no:',self.list_of_call_objects[i].called_num)
         print('durtaion:',self.list_of_call_objects[i].duration)
         print('type',self.list_of_call_objects[i].type)
         if self.list_of_call_objects[i].type=='STD':
            self.std+=1
         elif self.list_of_call_objects[i].type=='ISD':
            self.isd+=1
         elif self.list_of_call_objects[i].type=='Local':
            self.local+=1
         print('NO OF STD CALLS',self.std)
         print('NO OF ISD CALLS',self.isd)
         print('NO OF local CALLS',self.local)
     def person_details(self):
       p=input('enter phone no modified')
       for i in range(len(self.list_of_call_objects)):
         if self.list_of_call_objects[i].calling_num==p:
           print('called no:',self.list_of_call_objects[i].called_num)
           print('durtaion:',self.list_of_call_objects[i].duration)
           print('type',self.list_of_call_objects[i].type)
           print('................')
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
Util_obj=Util()
Util_obj.parse_customer(list_of_call_string)
Util_obj.display()
Util_obj.person_details()
