from j2l.pyrobotx.robot import IRobot, RobotEvent
import j2l.pyrobotx.client as ova
import cv2

import os
#os.system("pip install requests")
import random
import time
import pygame

from deplacement.deplacement import *

# Pour piloter une ova sur un LAN ou si vous êtes directement connecté à son point d'accès
robot:IRobot = ova.OvaClientHttpV2(url="192.168.71.1") 

# Appel de la callback onRobotEvent pour chaque évènements du robot
def onRobotEvent(source, event, value):
	print("Rx event", event, "from", source, ":", value)

robot.addEventListener(RobotEvent.imageReceived, onRobotEvent)
robot.addEventListener(RobotEvent.robotChanged, onRobotEvent)
robot.addEventListener(RobotEvent.robotConnected, onRobotEvent)
robot.addEventListener(RobotEvent.robotDisconnected, onRobotEvent)


pygame.init()
window = pygame.display.set_mode((400, 350))

robot.update()
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False    
	keyQ = pygame.key.get_pressed()

	fleche_avant = keyQ[pygame.K_UP]
	fleche_arriere = keyQ[pygame.K_DOWN]
	fleche_droite = keyQ[pygame.K_RIGHT]
	fleche_gauche = keyQ[pygame.K_LEFT]
	
	### ECRIVEZ CI-DESSOUS POUR FAIRE AVANCER VOTRE ROBOT ###
	### Indice : Utilisez avance(robot), recule(robot), droite(robot) et gauche(robot)
	


	### NE PAS MODIFIER CI-DESSOUS ###

	if [keyQ[pygame.K_DOWN], keyQ[pygame.K_UP], keyQ[pygame.K_RIGHT], keyQ[pygame.K_LEFT]] == [0,0,0,0]:
		stop(robot)

pygame.quit()
robot.stop()
robot.update()

