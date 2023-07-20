class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name
	@property
	def name(self):
		print("Inside getter")
		return self.hidden_name

	@name.setter
	def name(self, imput_name):
		print("inside setter")
		self.hidden_name = imput_name

	name = property(get_name, set_name)


don = Duck('Donald')
print(don.get_name())

don.set_name('Donna')
print(don.get_name())

d1 = Duck('Daisy')
print(d1.name)
d1.name = 'George'
print(d1.name) # George

class Circle():
	def __init__(self, radius):
		self.radius = radius

	@property
	def diameter(self):
		return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 6
print(c.radius)
print(c.diameter)