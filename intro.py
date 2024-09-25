"""
Hello this is used for docs
"""

name = "Ashish Sapkota"
age = 26
job = True
married = False 
hobbies = ["cycling", "music", "football"]
events = {
    "jan": "went to kolkatta",
    "feb": "swimming",
}
my_mood = { "happy", "sad", "joy", "excited", "joy"}

print(my_mood)

class Bike():
    name = "Beneli"
    cc = 300
    
    def __str__(self) -> str:
        return self.name

beneli = Bike()

print("name:", name)
print("beneli:", beneli)



