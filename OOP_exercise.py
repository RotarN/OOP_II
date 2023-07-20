class user_profile():
	def __init__(self, first_name, last_name, age=None, password=None):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.password = password

	def describe_user(self):
		print(f'Info user :{self.first_name}, {self.last_name} \n age {self.age}')

	def greet_user(self):
		print(f'Welcome back {self.first_name} {self.last_name}')


user1 = user_profile('Alex', 'Pap')
user2 = user_profile('George', 'Balint', 23)
user3 = user_profile('Ana', 'Codrea', 30, 300)
user4 = user_profile('Billy', 'Bob', 40, 'Bozo123')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()