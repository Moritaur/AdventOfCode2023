# Author: David Emmons
# Advent of Code 2023 day 3

filename = 'data3.txt'
engine_schematic = {}
with open(filename, "r") as infile:
	i = 0
	for line in infile:
		engine_schematic[i] = line.strip()
		i += 1


def main(engine_schematic):
	"""Main function"""
	total = 0
	for cur_line in engine_schematic:
		lines_to_check = []
		# Select the previous, current, and next lines of the engine schematic
		if cur_line > 0:
			previous_line = engine_schematic[cur_line - 1]
			lines_to_check.append(previous_line)
		line_data = engine_schematic[cur_line]
		lines_to_check.append(line_data)
		if cur_line < len(engine_schematic) - 1:
			next_line = engine_schematic[cur_line + 1]
			lines_to_check.append(next_line)
		i = 0
		check_min = 0
		check_max = 0
		# iterate over the current line, find valid numbers, check previous, cur, and next lines for symbols
		while i < len(engine_schematic[cur_line]):  # Iterate through the line and look for symbols anything != '1234567890.'
			if line_data[i] in '1234567890':  # This is a usable number check this line, and the line above and below.
				# find range of number, determine range of "surrounding numbers".
				check_min, check_max = find_range(line_data, i)
				# Check the min and max area for symbols in current, above, and below lines.
				for line in lines_to_check:
					add = False
					for j in range(check_min, check_max + 1):
						if line[j] not in '1234567890.':
							add = True
							break
					if add is True:
						total += int(line_data[check_min + 1:check_max])
						break
				i = check_max
			i += 1

	return total



def find_range(line, index):
	"""This function will take the indicies of a number and the line they are in, return all the values
	that need to be checked for a symbol."""
	start_index = index
	if start_index > 0:
		start_index -= 1
	end_index = index
	while line[end_index] in '1234567890' and end_index < len(line) - 1:
		end_index += 1
	return start_index, end_index


print(main(engine_schematic))
