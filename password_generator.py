import string
import random

while True:
	try:
		length = int(input("Enter password length: "))
		break
	except ValueError:
		print("This doesn't look like a number to me")



low_caps = list(string.ascii_lowercase)
big_caps = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

while True:
	try:
		characters_number = int(length)

		if characters_number < 8:
			print("Your password length should be at least 8.")
			length = input("Enter password length: ")
		else:
			break

	except:
		print("Please enter a number.")

		length = input("Enter password length: ")

random.shuffle(low_caps)
random.shuffle(big_caps)
random.shuffle(numbers)
random.shuffle(symbols)

part1 = round(length * (30/100))
part2 = round(length * (20/100))

result = []

for x in range(part1):
	result.append(low_caps[x])
	result.append(big_caps[x])

for x in range(part2):
	result.append(numbers[x])
	result.append(symbols[x])

random.shuffle(result)

password = "".join(result)
print("Strong Password: ", password)
