# Harjutus 3
# Kevin Joarand
# 14.04.2022

extends Node    
 
func _ready():
	var elud1 = 100
	var elud2 = 100
	for x in range(8,15):
		elud1 -= x
		print("P1 Life: ", elud1," Hit: ", x)
	for y in range(8,15):
		elud2 -= y
		print("P2 Life: ", elud2," Hit: ", y)
