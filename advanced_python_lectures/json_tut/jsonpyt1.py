from json import JSONEncoder
import json
from os import name, system

system("cls")
print("...JSON...")
print("-"*15)

# ENCODE JSON


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)


# Encoding JSON
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = UserEncoder().encode(user)
print(type(userJSON))
print(userJSON)


# Decoding JSON
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print("Name : ", user.name, "- Age : ", user.age)
