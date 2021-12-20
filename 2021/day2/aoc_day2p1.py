# Allison Chanin
# advent of code day #2

def main():
	with open ("positionchanges.txt") as file:
		commands = file.readlines()
		depth, horizontal_position = movements(commands)
		print (depth * horizontal_position)

def movements(position_changes):
	depth = 0
	horizontal_position = 0
	for command in position_changes:
		command = command.rstrip(" \n")
		if command[:7] == "forward":
			horizontal_position += int(command[-1])
		elif command[:4] == "down":
			depth += int(command[-1])
		elif command[:2] == "up":
			depth -= int(command[-1])
	return depth, horizontal_position

main()

