class Hotel():
    def __init__(self,name_hotel,place,rooms_mid,mid_room_price,rooms_lux,lux_room_price):
        self.name_hotel = name_hotel 
        self.place = place 
        self.rooms_mid = {"room1": "free", "room2": "free", "room3": "free"}
        try: 
            self.mid_room_price = disc_mid
        except NameError:    
            self.mid_room_price = mid_room_price
        self.rooms_lux = {"room1": "free", "room2": "free", "room3": "free"}
        try:
            self.lux_room_price = disc_lux
        except NameError:
            self.lux_room_price = lux_room_price   
    def presentation_hotel(self):
        return f"the hotel's name is {self.name_hotel}, it is located in {self.place},it has 3 mid rooms and the price for mid room is {self.mid_room_price} it also has 3 luxury rooms and the price is {self.lux_room_price}"
    def booking(self,room_number,room_type):
        if room_number == 1 and room_type == "mid":
            self.rooms_mid["room1"] = "bussy"
        elif room_number == 1 and room_type  == "lux":
            self.rooms_lux["room1"] = "bussy"
        elif room_number == 2 and room_type == "mid":
            self.rooms_mid["room2"] = "bussy"
        elif room_number == 2 and room_type == "lux":
            self.rooms_lux["room2"] = "bussy"
        elif room_number == 3 and room_type == "mid":
            self.rooms_mid["room3"] = "bussy"
        elif room_number == 3 and room_type == "lux":
            self.rooms_lux["room3"] = "bussy"
        else:  
            print("there is no such room")
    def available_room_check(self):
        counter = 0
        counter_ = 0
        for i in self.rooms_mid:
            if self.rooms_mid[i] == "free":
                counter +=1
        for i in self.rooms_lux:
            if self.rooms_lux[i] == "free":
                counter_ +=1
        return print(f"there are {counter} rooms free and {counter_} lux rooms free right now.")
    def discount_hotel(self,percent):
        global disc_mid , disc_lux 
        disc_mid = self.mid_room_price / 100 * (100-percent)
        disc_lux = self.lux_room_price / 100 * (100-percent)

class Taxi(Hotel):
    def __init__(self,name_taxi,car_types,price_for_tour,**kwds):
        self.name_taxi = name_taxi
        self.car_types = car_types
        try:
            self.price_for_tour = discount_taxi
        except NameError:
            self.price_for_tour = price_for_tour
        super().__init__(**kwds)
    def presentation_taxi(self):
        return f"the name of taxi company is {self.name_taxi} our cars are {self.car_types} and the price for the tour is {self.price_for_tour}" 
    def discount_taxi(self,percent):
        global discount_taxi 
        discount_taxi = self.price_for_tour / 100 * (100- percent) 
       

class Tour(Taxi,Hotel):
    def __init__(self,name_tour,price_lux, price_mid,**kwds):
        super().__init__(**kwds)
        self.name_tour = name_tour
        self.price_lux = self.lux_room_price + self.price_for_tour 
        self.price_mid = self.mid_room_price + self.price_for_tour
        
    def presentation(self):
        return f"Hello we offer {self.name_tour} tour we have two options {self.price_lux} and {self.price_mid},\
 which includes transport {super().presentation_taxi()}. You will stay at the hotel and {super().presentation_hotel()}"


check = Tour(name_tour= "Geghard",price_lux = None,price_mid =None, name_taxi = "Ani",car_types = "bmw",price_for_tour = 10000,name_hotel = "Lerane",place = "Geghard",rooms_mid = None, mid_room_price = 10000, rooms_lux=  None, lux_room_price = 20000)
check.discount_taxi(30)
check.discount_hotel(30)
check = Tour(name_tour= "Geghard",price_lux = None,price_mid =None, name_taxi = "Ani",car_types = "bmw",price_for_tour = 10000, name_hotel = "Lerane",place = "Geghard",rooms_mid = None, mid_room_price = 10000, rooms_lux=  None, lux_room_price = 20000)
print(check.presentation())

















