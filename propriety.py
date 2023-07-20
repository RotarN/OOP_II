class Duck():
	def __init__(self, input_name):
		self.__name = input_name

	@property
	def name(self):
		print("Inside getter")
		return self.__name

	@name.setter
	def name(self, imput_name):
		print("inside setter")
		self.__name = imput_name


d1 = Duck("Daisy")
print(d1.name)
d1.name = "George"
print(d1.name)