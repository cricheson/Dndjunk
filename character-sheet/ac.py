from stats import *




class WhatsMyAC(object):
	def __init__(self, player_stats):
		self.player_stats = player_stats

	def ac_calc(self):
		self.dexmod = self.player_stats.dex.modifier
		self.base = 10
		self.conmod = self.player_stats.con.modifier
		return 10 + self.dexmod() + self.conmod()