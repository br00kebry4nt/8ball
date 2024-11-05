#eightball.py
import random

inventories = [
    "unfortunately no",
    "signs point to yes",
    "the future's uncertain",
    "my sources say no",
    "undeniably certain",
    "keep your options open",
    "the odds are stacked against you",
    "your future looks bright" ]

print("Which fate will you choose?")
print("1: all possibilities")
print("2: mere certainty")
print("3: take a chance")

response = input("Please choose 1,2, or 3:")

if response == '1':
    print("your fates")
    for (id, inventory) in enumerate(inventories):
        print(f"{id}: {inventory}")
    
if response == '2':
    number = int(input("which number would you like? (0-7): "))
    if number in range(8):
        print(inventories[number])
    else:
        print("please enter a number between 0 and 7.")
    
if response == '3':
    question = input("your question: ")
    random_index = random.randint(0, len(inventories) - 1)
    print(inventories[random_index])