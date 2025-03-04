my_string: str = "Hello World"
modified_string: str = my_string.split("l")
print(modified_string)

message : str= "Pakistan won all the matches of champions trophy!, Pakistan"
message = message.replace("Pakistan", "India")
print(message)

join_with =  ", "
cricket_team_countries: str = join_with.join(["Pakistan", "India", "USA"])
print(cricket_team_countries)

name: str = "Shiza"
print(len(name))

name = "Shiza";
print(id(name))

import sys
# # a = sys.intern("hello world")
# # b = sys.intern("hello world")
# a= "hello world"
# b = "hello world"
# print(id(a))
# print(id(b))
# print(a is b)
a = "hello"
b = "world"
c = "helloworld"
d = sys.intern(a + b)
print(c is d)

string_methods: str = dir(str)
filtered_methods: str = [method for method in string_methods if not method.startswith("__")]
filtered_methods

fruits: list = ["Mango", "Grapes", "Banana"]
# print(fruits[0: 1])
# fruits.append("Orange" )
# fruits.append("Pineapple")
# fruits.append("Kiwi")
# fruits.append("Water melon")
fruits.extend(["Orange", "Pineapple", "Kiwi", "Water melon"])
fruits.pop(3)
print(fruits)

person : dict = {

    "name": "Shiza",
    "age": 21,
    "isTeacher" : True,
    "class": {
        "timings": "2 to 5",
        "day": "Saturday"
    }
}
print(person['class']['timings'])

import random
babar_score: int = random.randint(0, 120)
if(babar_score > 50):
  print("👑", "KING" )
else:
  print("🔔","KING")

  cricket_team_players = ("Babar Azam", "Rizwan", "Shaheen Afridi")
# cricket_team_players[1] = "Sarafraz Ahmed"
print(cricket_team_players)

value: set = {0, 1, 2, 4, 1, 2}
print(value)

fruits: set = {"Mango", "Grapes", "Banana", "Mango"}
print(type(fruits))