# Harjutus 01
# Kevin Joarand
# 13.04.2022
 
extends Node    

func _ready():
	var nimi = "Valdis"
	var elud = 100
	
 #Teksti kuvamine
	print(nimi)
	print("Elusid on: ",elud)
#Teksti pikkuse kuvamine (len = teksti pikkus) 
	print("Nime pikkus on: ", len(nimi))
#Genereerib suvalise arvu
	print("Suvaline arv: ",randi() % 19)
#Mängija elude arv kui saab +2 elu
	elud += 2
	print("Elude arv pärast +2 elu: ",elud) 
