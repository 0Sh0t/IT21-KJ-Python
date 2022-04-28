#Kevin Joarand
#Harjutus 04
#20.04.2022

extends Node

func _ready():
	var player = {"name":"Vello", "posx":69, "posy":420, "health":100, "items":["Mõõk","Obene"], "kuld":0}
	
	print(player.kuld)
	for i in range(5):
		player.kuld += 5
		print("+5 Kulda")
	print(player.kuld)
