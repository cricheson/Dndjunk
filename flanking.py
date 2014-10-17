#still needs funtionality for bigger monsters / multiple squares

fighter = (1,1)
orc = (3,3)
rogue = (5,5)

def distance(a, b):
	x = a[0] - b[0]
	y = a[1] - b[1]
	return (x, y)

def next_to(a, b):
	dist = distance(a, b)
	if(abs(dist[0]) is 1 and abs(dist[1]) is 1):
		return True
	else:
		print ("items are too far apart")
		return False

		
def is_flanking(player1, monster, player2):
	dist1 = distance(player1, monster)
	dist2 = distance(player2, monster)
	print (dist1)
	print (dist2)
	
	if (dist1[0] + dist2[0] == 0) and (dist1[1] + dist2[1] == 0) and (next_to(player1, monster)):
		print ("they are flanking")
		return True
	print ("they are not flanking")
	return False
	

print ("Are fighter and rogue flanking the orc {0}".format(is_flanking(fighter, orc, rogue)))
