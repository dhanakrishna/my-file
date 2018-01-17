#!/usr/bin/python3
class A:
	def __init__(self,name,place,age):
		self.name = name
		self.place = place
		self.age = age
	def Display(self):
		return"name:{}\nplace:{}\nage:{}\n".format(self.name,self.place,self.age)


	@classmethod
	def dis(cls,string):
		name,place,age = map(str,string.split('-'))
		x = cls(name,place,age)
		return x
	@staticmethod
	def disp(string):
		name,place,age = map(str,string.split('-'))
		return name == 'dhana' and place == 'kakinada' or age >= '24'

q = A.dis('dhana-kakinada-24')
print(q.Display())
w = A.disp('dhana-kakinada-25')
print(w)
