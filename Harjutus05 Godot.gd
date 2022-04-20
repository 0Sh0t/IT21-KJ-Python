#Kevin Joarand
#Harjutus 05
#20.04.2022

extends Node
 
func _ready():
 pass
 
func _process(delta):
 pass
func ylesanne():
	var tootunnid = 10
	var tunnid = 40
	var tunnitasu = 10
	var tasu = tunnid*tunnitasu
	if tunnid >= 40:
		print(tasu)
	elif tunnid < 40:
		tasu = 40*tunnitasu+(tunnid-40)*1.5*tootunnid
		print(tasu)
