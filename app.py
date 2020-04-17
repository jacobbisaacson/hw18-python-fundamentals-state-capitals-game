# print('hw18')
from capitals import states
import random
# print(states)
for state in states:
	state['correct'] = 0
	state['incorrect'] = 0

random.shuffle(states)
# print(states)
# def 
app_score = 0
app = True
while app:
	app_start = input("Play the state capitals game? (y to start)")
	if app_start == "y":
		print ("nice!  this is better than sporcle anyway")
		for state in states:
			answer = input(f"type the capital of {state['name']}: ")
			if answer == state["capital"]:
				state['correct'] += 1
				app_score += 1
				print("correct! you is kind, you is smart, you is important")
				print(f"you have gotten {app_score} right! Keep going until you get all 50!")
			if answer != state["capital"]:
				state['incorrect'] += 1
				print("oooh sorry, wrong!")

				# HERE'S WHERE TO ASK FOR HELP
				# CAN'T JUST DO AN IF APP_SCORE = 5 (or 50) then ask input to play again...
		print("nice job! game over!")
		play_again = input("wanna play again? (y to restart)")


		if play_again == "y":
			app = True
		else:
			print("k fine bye!")
			app = False
							




