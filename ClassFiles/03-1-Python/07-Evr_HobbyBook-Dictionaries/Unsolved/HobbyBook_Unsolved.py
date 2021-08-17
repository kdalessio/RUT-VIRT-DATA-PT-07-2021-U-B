# @TODO: Your code here
pet = {"name": "John",
"age":7,
"hobbies":["sleeping","eating","tricks"],
"wakeup":{"Monday":6,"Friday":8,"Sunday":10}}

print(f"My dog's name is {pet['name']} and is {pet['age']} years old.")
print(f"My dog has {len(pet['hobbies'])} hobbies.")
print(f"My dog's favorite hobby is {pet['hobbies'][0]}.")
print(f"My dog wakes up at {pet['wakeup']['Monday']} on Mondays.")