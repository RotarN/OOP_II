import random


class Dice():
	def __init__(self, num=6):
		self.num = num

	def aruncare_zar(self):
		return random.randint(1, self.num)


zar6 = Dice()
zar10 = Dice(10)
zar20 = Dice(20)

print([zar6.aruncare_zar() for i in range(10)])
print([zar10.aruncare_zar() for i in range(10)])
print([zar20.aruncare_zar() for i in range(10)])
