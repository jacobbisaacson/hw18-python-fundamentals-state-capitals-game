print('hw18')
from capitals import states
import random
# print(states)

random.shuffle(states)
# print(states)

app = True
while app:
	app_start = input("Play the state capitals game? (y to start)")
	if app_start == "y":
		print ("nice!  this is better than sporcle anyway")
		answer = input(f"type the capital of {states[0]['name']}: ")
		if answer == states[0]["capital"]:
			print("correct! you is smart, you is kind, you is important")


