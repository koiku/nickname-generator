"""

* 0 - Vowel letter
*
* 1 - Consonant letter

"""

import random

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS = [
	'b', 'c', 'd', 'f', 'g',
	'h', 'j', 'k', 'l', 'm',
	'n', 'p', 'q', 'r', 's',
	't', 'v', 'w', 'x', 'z'
]
MIN_LEN = 3
MAX_LEN = 8


def main():
	length = random.randint(MIN_LEN, MAX_LEN)
	nickname = ""
	prev_letter = -1
	two_vowels = False
	for letter in range(length):
		
		if letter == 0:
			letter_type = random.randint(0, 1)
			prev_letter = letter_type
			if letter_type == 0:
				nickname += random.choice(VOWELS)
				two_vowels = False
			else:
				nickname += random.choice(CONSONANTS)
				two_vowels = False
			continue

		if prev_letter == 1:
			nickname += random.choice(VOWELS)
			prev_letter = 0
		elif prev_letter == 0:
			letter_type = random.randint(0, 1)
			if letter_type == 0 and not two_vowels:
				nickname += random.choice(VOWELS)
				two_vowels = True
			else:
				nickname += random.choice(CONSONANTS)
				two_vowels = False

	print(nickname)


if __name__ == "__main__":
	main()
