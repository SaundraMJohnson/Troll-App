
#This is the infographics of input, minus the print statements.
from sys import argv

def troll_loop1(user_name, likes, lives, computer, dog):
	print(f"Hi {user_name}")
	print("I'd like to ask you a few questions.")
	print(f"Do you like me {user_name}?")

likes = input(answer)

print(f"'Where do you live {user_name}?")
lives = input(answer)

print("What kind of computer do you have?")
computer = input(answer)

print(f"What kind of dog is {dog}?")
animal = input(answer)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Trash.
While having {dog}, the smelly {animal}?
Good luck in life buddy.
""")

answer = '> '

#This does not work 20210706, trying to refactor this into a working function.