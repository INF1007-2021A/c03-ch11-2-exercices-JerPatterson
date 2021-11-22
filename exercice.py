"""
Chapitre 11.3
"""


import math
from inspect import *

from game import *


def simulate_battle():
	c1 = Character("Äpik", 500, 150, 70, 70)
	c2 = Magician("Damn! That magic dude", 450, 100, 50, 150, 50, 65)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.spell = Spell("Big Chungus Power", 100, 35, 50)
	c2.weapon = Weapon("Slingshot", 80, 20)
	c2.using_magic = True

	turns = run_battle(c2, c1)
	print(f"The battle ended in {turns} turns.")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

