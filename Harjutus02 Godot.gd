# Harjutus 02
# Kevin Joarand
# 13.04.2022

extends Node

func _ready():
	var kogus = 5
	
	var toode = "Banaani piim"
	var tootehind = 5
	
	#v2ljastab palju isikul on raha
	print("Teil on ",kogus," eurot")
	#väljastab toote hinna ja nime
	print("Toode: ",toode," on ",tootehind," eurot")
	
	#prindib vastuse vastaval rahalisele olukorrale
	if kogus >= tootehind:
		print("teil on piisavalt raha, et osta toode: ",toode,". Teil jääb üle ",kogus - tootehind," eurot")
	else:
		print("Teil ei ole piisavalt raha, et osta toodet: ",toode,". Teil jääb puudu ",kogus - tootehind," eurot")
	
