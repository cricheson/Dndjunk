from stats import *
from skills import *
from ac import *

steve = Stats(21,16,12,13,14,16,9)
steve_skills = Skills(steve)
steve_ac = WhatsMyAC(steve)




#print steve.str.val
#print steve.str.modifier()
#print steve_skills.skill_dict['athletics']()
#print steve_skills.is_proficient('perception')
#print steve_skills.passive_perception_calc("no")
#print steve.lvl.val
#print steve.lvl.prof_bonus()
print steve_ac.ac_calc()