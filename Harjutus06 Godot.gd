extends Node

var vaenlane = 100
var salv = 5
var skoor = 0
var lask = 0
var pihtas = bool(randi() % 2)
var eff = 100
var rng = RandomNumberGenerator.new()
func _ready():
	print("----------------------------------")
	print("----------Tulista kolli-----------")
	print("-------------Kevin----------------")

func _process(_delta):
	$taustapilt/ammo.text = "Ammo: "+  str(salv)
	if Input.is_action_just_pressed("tulista"):
		if pihtas == true:
			print("piu piu")
			rng.randomize()
			var suv = rng.randi_range(8,12)
			vaenlane -= suv
			print("Vaenlase elud: ", vaenlane)
			skoor += 1
			print("Skoor: ", skoor)
			salv -= 1
			lask += 1
			
			print("Salves: ", salv)
		else:
			print('lasid mööda')
		if pihtas == false:
			eff = 100 - 10
		if vaenlane <= 0:
			print("------------Mäng läbi------------------")	
			get_tree().quit()
			
			print("Laskude arv: ", lask)
			print("Täpsus: ", eff)
			print("Skoor: ", skoor)
			
	
		
	if Input.is_action_just_pressed("lae"):
		print("laen")
		salv = 5
