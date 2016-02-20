##character sheet
class ComputedStat(object):
	def __init__(self, val):
		self.val = val

	def modifier(self):
		return self.val / 2 - 5


class Stats(object):

	def __init__(self, str, dex, con, int, wis, cha):
		self.str = ComputedStat(str)
		self.dex = ComputedStat(dex)
		self.con = ComputedStat(con)
		self.int = ComputedStat(int)
		self.wis = ComputedStat(wis)
		self.cha = ComputedStat(cha)

#	def getstrmod(self):
#		return self.str / 2 - 5
#
#	def getdexmod(self):
#		return self.dex / 2 - 5
#
#	def getconmod(self):
#		return self.con / 2 - 5	
#
#	def getintmod(self):
#		return self.int / 2 - 5
#
#	def getwismod(self):
#		return self.wis / 2 - 5

#	def getchamod(self):
#		return self.cha / 2 - 5


