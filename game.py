"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""


import random

import utils
from character import *
from magician import *


def deal_damage(attacker: 'Character', defender: 'Character') -> None:
	damages, critical = attacker.compute_damage(defender)
	if isinstance(attacker, Magician) and attacker.using_magic:
		print(f"{attacker.name} used {attacker.spell.name}")
	else:
		print(f"{attacker.name} used {attacker.weapon.name}")
	if critical:
		print("  Critical hit!")
	print(f"  {defender.name} took {damages} dmg")
	

def run_battle(c1: 'Magician', c2: 'Magician') -> int:
	turns = 0
	attacker, defender = c1, c2
	print(f"{attacker.name} starts a battle with {defender.name}!")

	while True:
		deal_damage(attacker, defender)
		if defender.hp <= 0:
			print(f"{defender.name} is sleeping with the fishes.")
			break
		attacker, defender = defender, attacker
		turns += 1
		
	return turns
