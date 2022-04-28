#Kevin Joarand
#Harjutus 04
#20.04.2022

extends Node

var mangijad = ["Feake","Bradwell","Dreger","Bloggett","Lambole","Daish","Lippiett","Blackie","Stollenbeck","Houseago","Dugall","Sprowson","Kitley","Mcenamin","Allchin","Doghartie","Brierly","Pirrone","Fairnie","Seal","Scoffins","Galer","Matevosian","DeBlase","Cubbin","Izzett","Ebi","Clohisey","Prater","Probart","Samwaye","Concannon","MacLure","Eliet","Kundt","Reyes"]

func _ready(): 
	print("Mängijate arv: ", len(mangijad))
	print("Esimene nimi: ", mangijad[0])
	mangijad.erase("Reyes")
	mangijad.append("Kevin")
	print(mangijad.max())
	print(mangijad)
