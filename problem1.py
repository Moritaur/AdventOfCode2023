# Author: David Emmons
# Advent of code 2023, problem 1

def replace_string_with_int(line):
	nums = {"one": '1', "two": '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
	        'eight': '8', 'nine': '9', 'zero': '0'}
	i = 0
	end = len(line)
	new_line = ''
	while i < end:
		line = line.lower()
		slice3 = line[i:i+3]
		slice4 = line[i:i + 4]
		slice5 = line[i:i + 5]
		if slice3 in nums:
			new_line += nums[slice3]
			i += 3
		elif slice4 in nums:
			new_line += nums[slice4]
			i += 4
		elif slice5 in nums:
			new_line += nums[slice5]
			i += 5
		else:
			if line[i] in "1234567890":
				new_line += line[i]
			i += 1
	return new_line

with open("data1.txt", "r") as data:
	total = 0
	for line in data:
		new_line = replace_string_with_int(line)
		num1 = 0
		num2 = 0
		for i in range(len(new_line)):
			if num1 == 0:
				num1 = new_line[i]
				num2 = new_line[i]
			else:
				num2 = new_line[i]
		new_num = num1 + num2
		total += int(new_num)
		print(line, new_line, new_num)
	print(total)

import re

"""
    Not super proud of the part 2 solution due to the many nested for() loops.
"""

filename = "data1.txt"
input = []
with open(filename) as file:
	input = [line.strip() for line in file.readlines()]


def part1():
	total = 0
	for line in input:
		line = re.sub('\D', '', line)  # remove non-digits from string
		nums = int(line[0] + line[-1])  # retain only first and last digit, convert to integer
		total += nums  # add to running total
	return total


def part2():
	values = {
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9"
	}
	pairs = []
	for line in input:
		digits = []
		# start at the first letter and move through it letter by letter.
		# this is the only way i've found to account for overlapping words.
		# an example is "oneight", which only matches "one" when using re.findall.
		for i, c in enumerate(line):
			if line[i].isdigit():
				digits.append(line[i])
			else:
				for k in values.keys():
					if line[i:].startswith(k):
						digits.append(values[k])
		pairs.append(int(f"{digits[0]}{digits[-1]}"))

	return sum(pairs)


print("Part one:", part1())
print("Part two:", part2())