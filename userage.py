
import datetime

name = input("please type your name: ").capitalize()
print()
age = int(input("please enter in your age: "))
print()
year = datetime.date.today().year

oldIn = year - age + 100

print()

print(f"{name} you will be 100 years old in {oldIn}")   