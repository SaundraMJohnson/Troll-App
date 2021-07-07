

def infographics1(age, height, weight):
	print(f"""
		So, let me get this straight... you're {age} 
		years old, {height} inches tall, and {weight} 
		pounds?
		""" )

def infographics2(user_name, likes, address, employer, age):
	print(f"""
		Alright, so you said {likes} about liking me.
		You live in {address}. Sounds dirty.
		And you work at {employer}. Depressing.
		All while being {age} years old?
		Good luck in life buddy.
			""")

answer = '> '

user_name = print("First things first, What is your name? ")
user_name = input(answer)
print(f"Hi {user_name}, I'd like to ask you a few questions.")

age = input("How old are you? ")
height = input("How tall are you? (in inches) ")
weight = input("How much do you weigh? ")

infographics1(age, height, weight)

likes = input(f"Do you like me already {user_name}? ")
address = input("Where do you live? ")
employer = input("Where do you work?")

infographics2(user_name, likes, address, employer, age)
