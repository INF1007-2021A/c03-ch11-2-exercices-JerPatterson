"""
Chapitre 11.3

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import *


# TODO: Créer la classe Spell qui a les même propriétés que Weapon, mais avec un coût en MP pour l'utiliser
class Spell(Weapon):
	"""
	Un sort dans le jeu.

	:param name: Le nom du sort
	:param power: Le niveau d'attaque
	:param mp_cost: Le coût en MP d'utilisation du sort
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	def __init__(self, name, power, mp_cost, min_level):
		super().__init__(name, power, min_level)
		self.mp_cost = mp_cost
		
	

# TODO: Déclarer la classe Magician qui étend la classe Character
class Magician(Character):
	"""
	Un utilisateur de magie dans le jeu. Un magicien peut utiliser des sorts, mais peut aussi utiliser des armes physiques. Sa capacité à utiliser des sorts dépend 

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param max_mp: MP maximum
	:param attack: Le niveau d'attaque physique du personnage
	:param magic_attack: Le niveau d'attaque magique du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage

	:ivar using_magic: Détermine si le magicien tente d'utiliser sa magie dans un combat.
	"""

	def __init__(self, name: str, max_hp: int, max_mp: int, attack: int, magic_attack: int, defense: int, level: int) -> 'Magician':
		# Initialiser les attributs de Character
		super().__init__(name, max_hp, attack, defense, level)
		# Initialiser le `magic_attack` avec le paramètre, le `max_mp` et `mp` de la même façon que `max_hp` et `hp`, `spell` à None et `using_magic` à False.
		self.max_mp = max_mp
		self.__mp = max_mp
		self.__spell = None
		self.magic_attack = magic_attack
		self.using_magic = False

	@property
	def mp(self):
		return self.__mp

	@mp.setter
	def mp(self, proposed_value: int):
		self.__mp = utils.clamp(proposed_value, 0, self.max_mp)

	# Écrire les getter/setter pour la propriété `spell`.
	#       On peut affecter None.
	#       Si le niveau minimal d'un sort est supérieur au niveau du personnage, on lève ValueError.
	@property
	def spell(self):
		return self.__spell

	@spell.setter  
	def spell(self, proposed_value: 'Spell'):
		if proposed_value.min_level > self.level:
			raise ValueError(Spell)
		self.__spell = proposed_value

	#  Surcharger la méthode `compute_damage` 
	def compute_damage(self, defender: 'Magician'):
		# Si le magicien va utiliser sa magie (`will_use_spell()`):
			# Soustraire à son MP le coût du sort
			# Retourner le résultat du calcul de dégâts magiques
		if self.will_use_spell():
			damages, critical = self._compute_magical_damage()
			self.mp -= self.spell.mp_cost
			defender.hp -= damages
			return damages, critical
		# Sinon
			# Retourner le résultat du calcul de dégâts physiques
		else:
			damages, critical = self._compute_physical_damage(defender)
			defender.hp -= damages
			return damages, critical

	def will_use_spell(self):
		return self.using_magic and self.spell is not None and self.mp >= self.spell.mp_cost

	def _compute_magical_damage(self):
		critical = random.random() <= 1/8
		modifier = (2 if critical else 1) * random.uniform(0.85, 1.0)
		damages = ((2 * (self.level + self.magic_attack) / 5 + 2) * self.spell.power / 50 + 2) * modifier
		
		return damages, critical

	def _compute_physical_damage(self, other):
		# Calculer le dommage physique exactement de la même façon que dans `Character`
		return super().compute_damage(other)

