# 1. Create a class named Sudent, which will inherit the properties and methods from the Person class.
# About attributes you can improvize
class Person:
	def __init__(self, sex, age, profession):
		self.sex = sex
		self.age = age
		self.profession = profession
	def thirteenold(self):
		sex = 'male'
		age = 19
		profession = "Student"
		return sex, age, profession
	def thirthold(self):
		sex = "male"
		age = 30
		profession = "accountant"
		return sex, age, profession
class Student(Person): 
	def presentation(self):
		if self.age > 25:
			print("not a student")
		else:
			print("he might be a student")


check = Student(0,0,0)
second_stage = check.thirteenold()
third_stage = Student(second_stage[0], second_stage[1], second_stage[2])
third_stage.presentation()
forth_stage = check.thirthold()
fifth_stage = Student(forth_stage[0], forth_stage[1], forth_stage[2])
fifth_stage.presentation()

# 2.
class Country:
	def __init__(self,name,continent):
		self.name = name
		self.continent = continent
	def Return_name(self):
		return name,continent
class Brand:
	def __init__(self,brand_name, start_date):
		self.brand_name = brand_name
		self.start_date = start_date
	def presentation(self):
		return f"{brand_name} was created {start_date}. "
class Season:
	def __init_(self,season_name, average_temperature):
		self.season_name = season_name
		self.average_temperature = average_temperature
	def presentation_season(self):
		return f"in {season_name} the average temperature is {average_temperature}"
class Product(Country, Brand, Season):
	def __init(self, product_name, product_type, product_price, product_quantity):
		self.product_name = product_name
		self.product_type = product_type
		self.product_price = product_price
		self.product_quantity = product_quantity
		Country.__init__(self, name, continent)
		Brand.__init__(self, brand_name, start_date)
		Season.__init__(self, season_name, average_temperature)
	def present_product(self):
		return print(f"this is {product_name} it is {product_type} the price is {product_price} and we have {product_quantity} left.")

	def discount(self, discount_persenatge):
		product_price = product_price / 100 * (100- discount_persenatge)
		return product_price
	def quantity_increase(self):
		product_quantity = product_quantity + 10 
		return product_quantity

check = Product("belt", "accesories", 500, 24, "USA", "america", "Gucci", 1965, "winter", 3)















