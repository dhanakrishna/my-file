
#!/usr/bin/python3
class A:
	def __init__(self,name,place):
		self.__college()
		self.__college2()
		self.name = name
		self.place = place
	def college1(self):
		return"name:{}\nplace:{}\n".format(self.name,self.place)
	def __college(self):
		print("Aditya college")
	def __college2(self):
		print("sri aditya college")


q = A("dhana","kakainada")
print(q.college1())
