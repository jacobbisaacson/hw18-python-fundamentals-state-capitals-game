print('hw18')
from capitals import states
import random
# print(states)
for state in states:
	state['correct'] = 0
	state['incorrect'] = 0

random.shuffle(states)
# print(states)

app = True
while app:
	app_start = input("Play the state capitals game? (y to start)")
	if app_start == "y":
		print ("nice!  this is better than sporcle anyway")
		for state in states:
			answer = input(f"type the capital of {state['name']}: ")
			if answer == state["capital"]:
				print("correct! you is smart, you is kind, you is important")



