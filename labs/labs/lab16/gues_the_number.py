import random

# --------------------------- functions definitions -------------------------- #
def genarate_machine_number(x=1,y=100):
	return random.randint(x,y)


def get_user_number(x,y):
	while True:
		try:
			user_number= int(input(f'Enter a number in range [{x},{y}]:'))
			print(user_number)
			if x<=user_number<=y:
				return user_number
			else:
				raise Exception("Number not in interval")

		except Exception as e:
			print(f'Error: {e}')

def user_move():
	user_number = get_user_number(start,end)
	global max_moves
	global user_win

	if machine_number == user_number:
		user_win = True
		game_end()
	elif user_number<machine_number:
		max_moves-=1
		print(f'up')
	else:
		print(f'down')
		max_moves-=1

def game_end():
	if user_win:
		print('Bravo, you win!!!!!')
	else:
		print('You loose')

def game_play():
	# while user is not win or max_moves is not reached:
	while not user_win or max_moves>=0:
		user_move()


# ------------------------------- main program ------------------------------- #
start = 1
end = 10

max_moves = 5
user_win = False

machine_number = genarate_machine_number(start, end)
# print(f'machine_number={machine_number}')
game_play()
