extends Node

var vaenlane = 100
var salv = 5
var skoor = 5
var lask = 10
var pihtas = bool(randi() % 2)
var eff = 100
var rng = RandomNumberGenerator.new()
func _ready():
	print("----------------------------------")
	print("----------Tulista kolli-----------")
	print("-------------Kevin----------------")

func _process(_delta):
	if Input.is_action_just_pressed("tulistamine"):
		if pihtas == true:
			print("piu piu")
			rng.randomize()
			var suv = rng.randi_range(8,12)
			vaenlane -= suv
			print("elud: ", vaenlane)
			skoor += 1
			print("Score: ", skoor)
			salv -= 1
			lask += 1
			
			print("ammo: ", salv)
		else:
			print("lasid mööda")
		if pihtas == false:
			eff = 100 - 10
		if vaenlane <= 0:
			print("------------Mäng läbi------------------")	
			get_tree().quit()
			
			print("Laskude arv: ", lask)
			print("Täpsus: ", eff)
			print("Skoor: ", skoor)

	if Input.is_action_just_pressed("lae"):
		print("reload")
		salv = 5
