# Author: David Emmons
# Advent of code 2023, problem 2
import re


# Function to clean each list
def clean_list(lst):
	cleaned_list = []
	for item in lst.split(','):
		# Strip and find all matches of the pattern (number followed by color)
		matches = re.findall(r'\d+ \b(?:blue|green|red)\b', item.strip())
		cleaned_list.extend(matches)
	return cleaned_list


# Function to split the input string and clean each part
def clean_and_split(input_string):
	lists = input_string.split(';')
	return [clean_list(lst) for lst in lists]


with (open("data2.txt", "r") as file):
	gameID = 1
	totalID = 0
	red = 12
	green = 13
	blue = 14
	powersetTotal = 0

	for line in file:
		count = 0
		# Get the final cleaned and structured lists
		final_cleaned_lists = clean_and_split(line)
		print(final_cleaned_lists)

		# Lists are returned in form "integer color"
		good_game = True
		fewest_cubes = {'red': 0, 'blue': 0, 'green': 0}
		for round in final_cleaned_lists:
			round_data = {'red': 0, 'blue': 0, 'green': 0}
			for datum in round:
				datum = datum.split(' ')
				blocks = datum[0]
				color = datum[1]
				cur_blocks = round_data[color]
				round_data[color] = int(blocks) + cur_blocks
			if round_data['red'] > red or round_data['blue'] > blue or round_data['green'] > green:
				good_game = False
			for color in round_data:
				fewest_cubes[color] = max(fewest_cubes[color], round_data[color])
		# Determine if there were enough blocks
		if good_game is True:
			totalID += gameID
		powersetTotal += fewest_cubes['red'] * fewest_cubes['green'] * fewest_cubes['blue']

		gameID += 1

	print(totalID, powersetTotal)