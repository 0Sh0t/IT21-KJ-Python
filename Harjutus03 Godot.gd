# Harjutus 03
# Kevin Joarand
# 14.04.2022

extends Node    
 
func _ready():
	var elud1 = 100
	var elud2 = 100
	for x in range(8,15):
		for y in range(5,10):
			elud1 -= x
			print("P1 Life: ", elud1," Hit: ", x)
			elud2 -= y
			print("P2 Life: ", elud2," Hit: ", y)
