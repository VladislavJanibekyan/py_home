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
        return f"{self.brand_name} was created {self.start_date}. "
class Season:
    def __init__(self,season_name, average_temperature):
        self.season_name = season_name
        self.average_temperature = average_temperature
    def presentation_season(self):
        return f"in {self.season_name} the average temperature is {self.average_temperature}"
class Product(Country, Brand, Season):
    def __init__(self, name, continent, product_name, product_type, product_price, product_quantity,brand_name, start_date, season_name, average_temperature):
        Country.__init__(self, name, continent)
        Brand.__init__(self,brand_name, start_date)
        Season.__init__(self,season_name, average_temperature)
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        self.product_quantity = product_quantity
    def present_product(self):
        return f"this is {self.product_name} it is {self.product_type} the price is {self.product_price} and we have {self.product_quantity} left."\
                F"the brand is {self.presentation()} the season is {self.presentation_season()}"
    def discount(self, discount_persenatge):
        self.product_price = self.product_price / 100 * (100- discount_persenatge)
        return self.product_price
    def quantity_increase(self):
    	self.product_quantity = self.product_quantity + 12 


check = Product("name_for_country", "value_for_continent","wine","drink", 2000, 12, "Armas","2010","Aoutumn","30",)

print("before modification ", check.present_product())
check.discount(30)
check.quantity_increase()

print("after modification ", check.present_product())















