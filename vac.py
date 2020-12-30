# 1. Write a Python program to create a dictionary from a string.
#  Note: Track the count of the letters from the string.
#  Sample string : ‘python’
#  Expected output: {‘p’: 1, ‘y’: 1, ‘t’: 2, ‘h’: 1, ‘o’: 1, ‘n’:1}
#  2․ Write a Python program to remove duplicate values from Dictionary.
#  3. Write a Python program to find the highest 3 values in a dictionary
#Էս երեքի համար պետք ա ունենաք մի հատ class որը իրա մեջ կունենա երեք մեթոդ, մեկը Dictionary սարքող, մեկը կրկնօրինակները ջնջող, մյուսը ամենամեծ 3 արժեքները գտնող
class Homework():
    def __init__(self, user_input, dic):
        self.user_input = user_input
        self.dic = dic
    def dec_meth(self):
        output = {}
        list_ = list(self.user_input)
        for i in self.user_input:
            output[i] = list_.count(i)
        return output
    def duplicate_val(self):
        for i in self.dic.copy():
            for j in self.dic.copy():
                if self.dic[i] == self.dic[j] and i != j:
                    self.dic[j] = 0
        return self.dic
    def highest_val(self):
        _list = []
        for i in self.dic:
            _list.append(self.dic[i])
        _list.sort()
        return _list[-3::]      
user = input()
b = Homework(user, None)
c = b.dec_meth()
dic = {"gi": 5, "df": 6, "sd": 4, "gh": 4, "third": 768, "forth": 534, 45: 54322, "Fsd": 234341}
d = Homework(user, dic)
print(b.dec_meth())
print(d.duplicate_val())
print(d.highest_val())

#4. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle():
    def __init__(self,radius):
            self.radius = radius
    def area(self):
        area_circle = (self.radius ** 2) * 3.14
        return area_circle
    def perimeter(self):
        perimeter_circle = 2 * 3.14 * self.radius 
        return perimeter_circle 


my_circle = Circle(4)


print(my_circle.area(), "this is the area" )
print(my_circle.perimeter(), "this is the perimeter")



# 5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
numbers= [10,20,10,40,50,60,70]
#  Output: 3, 4

class TN():
    def __init__(self, number, target):
        self.number = number
        self.target = target
    def pair(self):
        result = 0
        result_ = 0
        # for i in self.number:
        #     for j in self.number[1:]:
        #         if i + j == self.target and self.number.index(i) != self.number.index(j):
        #             result_ = self.number.index(i) + 1
        #             result = self.number.index(j) + 1
        for i in range(len(self.number)-1):
            if self.number[i] + self.number[i+1] == self.target:
                result = i + 1
                result_ = i + 2
        return result, result_


target_number = TN(numbers, 50)
print(target_number.pair())

                    





















































