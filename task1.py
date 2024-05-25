# class Shape:
#     def __init__(self, width, length):
#         self.width=width
#         self.length=length

# class Rectangle(Shape):
#      def get_perimetr(self):
#         return self.width*self.length
     
#      def get_area(self):
#         return 4*self.width

# class Square(Shape):
#     def get_perimetr(self):
#         return self.width*self.length
#     def get_area(self):
#         return 2*(self.width+self.length)
    
# o1=Square(2,4)
# print(o1.get_area())
# print(o1.get_perimetr())
# o2=Rectangle(2,4)
# print(o2.get_area())
# print(o2.get_perimetr)




# class Person:
#     def __init__(self, name, country, birth):
#         self.name=name
#         self.country=country
#         self.birth=birth
#     def age(self):
#         return f"name: {self.name}, country: {self.country}, birth:{self.birth}"
    
# agee=Person("Aziz", "Tajikistan", "18.08.2004")
# print(agee.age())

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category=category
#         self.year=year
#         self.winner=winner
#     def __str__(self):
#         return f"Category: {self.category}, year: {self.year}, winner: {self.winner}"
# np2004=Nobel("Peace", "2004", "Azizmurod Orifzoda")
# print(np2004.category, np2004.year, np2004.winner)

# class Staff:
#     def __init__(self, role,departament, salary):
#         self.role=role
#         self.departament=departament
#         self.salary=salary

# class Teacher(Staff):
#     pass


# a1=Teacher("Teacher", "yazik", "2000")
# print(a1.role, a1.departament, a1.salary)



class IceCream:
          
          def __init__(self, flavor, num_sprinkles):
              self.flavor = flavor
              self.num_sprinkles = num_sprinkles 

          
        
          
          def sweetest_icecream(self, my_list:list):
                 self.my_list=my_list
                 
          
