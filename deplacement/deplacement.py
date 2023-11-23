
def avance(robot, v=100, duree=100):
	robot.setMotorSpeed(-v, v, duree)
	robot.update()
	#robot.setMotorSpeed(0,0,0)
	#robot.update()
	
def recule(robot, v=100, duree=1):
	robot.setMotorSpeed(v, -v, duree)
	robot.update()
	#robot.setMotorSpeed(0,0,0)
	#robot.update()
	
def droite(robot, v=100, duree=100):
	robot.setMotorSpeed(v, v, duree)
	robot.update()
	#robot.setMotorSpeed(0,0,0)
	#robot.update()
	
def gauche(robot, v=100, duree=100):
	robot.setMotorSpeed(-v, -v, duree)
	robot.update()
	#robot.setMotorSpeed(0,0,0)
	#robot.update()
def stop(robot):
	robot.setMotorSpeed(0,0,0)
	robot.update()

def pas_a_pas(robot, direction="avant", v=30):
	z = (0,0)
	match direction:
		case "avant":
			z = (-v,v)
		case "arriere":
			z = (v,-v)
		case "droite":
			z = (v,v)
		case "gauche":
			z = (-v,-v)
		case _:
			print("ERREUR : L'argument direction doit valoir 'avant', 'arriere', 'droite' ou 'gauche'")
	robot.setMotorSpeed(z[0], z[1], 1)
	robot.update()
	robot.setMotorSpeed(0,0,0)
	robot.update()

"""Test pas_a_pas
robot.setLedColor(0, 255, 0)
robot.setMotorSpeed(-50,50,1)
robot.setMotorSpeed(0,0,0)
pas_a_pas(robot, "avant")
print("avant")
time.sleep(2)
pas_a_pas(robot, "arriere")
print("arriere")
time.sleep(2)
pas_a_pas(robot, "droite")
print("droite")
time.sleep(2)
pas_a_pas(robot, "gauche")
print("gauche")
time.sleep(2)
robot.setMotorSpeed(0,0,0)
robot.setLedColor(0, 0, 0)
robot.update()"""
