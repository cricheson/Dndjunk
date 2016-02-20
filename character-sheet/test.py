from stats import *
from skills import *

steve = Stats(15,16,12,13,14,16)
steve_skills = Skills(steve)


#print steve.getstr()

#skill_dict = {
#		'athletics': steve.getstrmod()
#	}

print steve.str.val
print steve_skills.skill_dict['athletics']()
print steve_skills.is_proficient('perception')
print steve_skills.passive_perception_calc("no")