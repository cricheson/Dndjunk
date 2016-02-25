from stats import *
## skills

class Skills(object):
	

	def __init__(self, player_stats):
		self.player_stats = player_stats


		self.skill_dict = {
			'athletics': self.player_stats.str.modifier,
			'acrobatics': self.player_stats.dex.modifier,
			'animal handling': self.player_stats.cha.modifier,
			'Deception': self.player_stats.cha.modifier,
			'history': self.player_stats.int.modifier,
			'insight': self.player_stats.wis.modifier,
			'intimidation': self.player_stats.cha.modifier,
			'investigation': self.player_stats.int.modifier,
			'medicine': self.player_stats.wis.modifier,
			'nature': self.player_stats.int.modifier,
			'perception': self.player_stats.wis.modifier,
			'performance': self.player_stats.cha.modifier,
			'persuasion': self.player_stats.cha.modifier,
			'religion': self.player_stats.int.modifier,
			'slight of hand': self.player_stats.dex.modifier,
			'stealth': self.player_stats.dex.modifier,
			'survival': self.player_stats.wis.modifier,
			'strength': self.player_stats.str.modifier,
			'dexterity': self.player_stats.dex.modifier,
			'constitution': self.player_stats.con.modifier,
			'intelligence': self.player_stats.int.modifier,
			'wisdom': self.player_stats.wis.modifier,
			'charisma': self.player_stats.cha.modifier,
	#		'passive_perception': self.player_stats.wis.modifier
		}

## Checks to see if you are proficient in a skill/stat/tool.
## Not sure how I want do define a characters proficiencies in the long run,
## but for now it is done in this function

	def is_proficient(self, player_skill):
		self.player_skill = player_skill
		profs = ['athletics','drugs']
		if player_skill in profs:
			return 3+self.skill_dict[player_skill]()

		else:
			return self.skill_dict[player_skill]()


	def passive_perception_calc(self, advantage):
		self.advantage = advantage

		if advantage is "yes":
			return 10+5+self.skill_dict['perception']()


		return 10+self.skill_dict['perception']()
