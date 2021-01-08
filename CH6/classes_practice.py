class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.favthings = []

  def introduction(self):
    print("{} is {} years old".format(self.name, self.age))

  def add_favourite(self,thing):
    self.favthings.append(thing)

  def show_favourites(self):
    for thing in self.favthings:
      print(f"{self.name} likes {thing}")




class Student(Person):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.modules = []
    self.loginid = ""

  def set_login(self,id):
    self.loginid = id

  def add_module(self,module):
    self.modules.append(module)

  def show_modules(self):
    print("{} is enrolled in:".format(self.name))
    for module in self.modules:
      print(module)


s = Student("Molly", 18)

s.introduction()
s.add_favourite("oranges")
s.add_favourite("French novels")
s.show_favourites()

s.add_module("MAS1801")
s.add_module("MAS1601")
s.show_modules()