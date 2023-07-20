class Animal():
	def says(self):
		return 'I speak'


class Horse(Animal):
	def says(self):
		return 'Iha'


class Donkey (Animal):
	def says(self):
		return 'Hee-haw'


class Mule (Donkey, Horse):
	pass


class Hinny (Horse, Donkey):
	pass

# print(Mule.mro())
# print(Hinny.mro())
donkey = Donkey()
print(donkey.says())
mule = Mule()
print(mule.says()) # ?  hee-haw
hinny = Hinny()
print(hinny.says()) #?  iha

class PrettyMixin():
	def dump(self):
		import pprint
		pprint.pprint(vars(self))


class Thing(PrettyMixin):
	pass


t = Thing()
t.name = "Nume"
t.feature = 'Feature'
t.age = 12
t.dump()
