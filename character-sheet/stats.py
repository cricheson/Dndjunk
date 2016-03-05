##character sheet
class ComputedStat(object):
	def __init__(self, val):
		self.val = val

	def modifier(self):
		return self.val / 2 - 5


class ProficiencyBonus(object):
	def __init__(self, val):
		self.val = val

	def prof_bonus(self):
		if self.val <= 4:
			return 2
		elif self.val <= 8:
			return 3
		elif self.val <= 12:
			return 4
		elif self.val <= 16:
			return 5
		else:
			return 6

class Stats(object):

	def __init__(self, str, dex, con, int, wis, cha, lvl):
		self.str = ComputedStat(str)
		self.dex = ComputedStat(dex)
		self.con = ComputedStat(con)
		self.int = ComputedStat(int)
		self.wis = ComputedStat(wis)
		self.cha = ComputedStat(cha)
		self.lvl = ProficiencyBonus(lvl)



