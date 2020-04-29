from capitals import states
from random import shuffle

for state in states:
	state['incorrect'] = 0
	state['correct'] = 0
shuffle(states)
# print(states)

game = True
while game:
	game_start = input("Play the state capitals game? (type y to start): ")
	if game_start == "y":
			print('Lets go!')
			for state in states:
				answer= input(f"Type the capital of {state['name']} and press enter: ")
				if answer == state["capital"]:
					state["correct"] += 1
					print("Nice!")
					print(f"You got it right {state['correct']} times! You got it wrong {state['incorrect']} times!")

				if answer != state["capital"]:
					state["incorrect"] += 1
					print("No, sorry!")
					print(f"You got it wrong {state['incorrect']} times! You got it right {state['correct']} times!")
			print("You win!!!!")
			game_play_again = input(f"Wanna play again? (type y to play again): ")
	else: 
		print("k, bye!")
		game = False



