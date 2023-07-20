class Fruit():
	color = 'red'

	def __init__(self, origine):
		self.__origine = origine

	@property
	def origine(self):
		return self.__origine


fx = Fruit('Mexic')
print(fx.origine)

f1 = Fruit()
print(f1.color)
print(Fruit.color)

f1.color = 'blue'
print(f1.color)
print(Fruit.color)

Fruit.color = 'orange'
print(f1.color)

f2 = Fruit()
print(f2.color)