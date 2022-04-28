#Kevin Joarand
#Harjutus 05
#28.04.2022

extends Node
var tasu = 0
var tunnid = 69
var tunnitasu = 10
var tootunnid = 40 
var eksamitulemused = []
var arv = 0

func random(a,b):
	var suva = RandomNumberGenerator.new()
	suva.randomize() 
	var suvaline = suva.randi_range(a,b)
	return suvaline

func tasu(tunnid, tunnitasu):
	if tunnid >= 40:
		tasu = tunnid*tunnitasu
	else: 
		tasu = 40*tunnitasu+(tunnid-40)*1.5*tootunnid
	tasu = round(tasu)
	print("Tasu: ",tasu, " | Tunde: ", tunnid)
	eksam(tunnid, tasu)
	
func eksam(tunnid, tasu):
	var punktid = 0
	if tunnid >= 40:
		punktid += 20
	elif tunnid >= 10:
		punktid += 5
	else:
		punktid += 10 
	
	if tasu >= 420:
		punktid += 40
	elif tasu >= 69:
		punktid += 5
	else:
		punktid += 10
	var suvaline = random(1,40)
	punktid += suvaline
	eksamitulemused.append(punktid)
	
	
func suvaline():
	for i in range(2):
		var suva = random(1,100)
		if arv == 0:
			tunnid = suva
			arv += 1
		else:
			tunnitasu = suva
	arv = 0
func keskmine():
	var keskmine = 0
	for i in eksamitulemused:
		keskmine += i
	keskmine = keskmine/len(eksamitulemused)
	return keskmine

func hinded():
	var hinded = []
	for i in eksamitulemused:
		if i >= 90:
			hinded.append(str(i)+" - 5")
		elif i >= 75:
			hinded.append(str(i)+" - 4")
		elif i >= 50:
			hinded.append(str(i)+" - 3")
		else:
			hinded.append(str(i)+" - 2")
	return hinded
	
func _ready():

	for i in range(5):
		suvaline()
		tasu(tunnid, tunnitasu)
	var keskmine = keskmine()
	print(keskmine)
	print(eksamitulemused)
	var hinded = hinded()
	print(hinded)
