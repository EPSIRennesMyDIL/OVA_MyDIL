from j2l.pyrobotx.robot import IRobot, RobotEvent
import j2l.pyrobotx.client as ova
import cv2

import os
#os.system("pip install requests")
import random
import time

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
import pygame

pygame.init()
window = pygame.display.set_mode((400, 350))

robot.update()
run = True
compteur = 50
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False    
	keyQ = pygame.key.get_pressed()

	### Le problème de lenteur semble venir de la réception des touches sur pygame, 
	# à voir si un autre système de réception des touches règlerait le problème.
	###

	###
	# TODO Ajout de la prise en compte de plusieurs touches simultanément (HAUT+DROITE pour aller en diagonale par exemple)
	###

	### Déplacement du robot avec le clavier ###
	if keyQ[pygame.K_UP] :
		avance(robot)
	if keyQ[pygame.K_DOWN] :
		recule(robot)
	if keyQ[pygame.K_RIGHT] :
		droite(robot)
	if keyQ[pygame.K_LEFT] :
		gauche(robot)

	if [keyQ[pygame.K_DOWN], keyQ[pygame.K_UP], keyQ[pygame.K_RIGHT], keyQ[pygame.K_LEFT]] == [0,0,0,0]:
		stop(robot)
	######

	### Détection de la luminosité pour envoyer des signals d'alerte en cas de franchissement de zones noires ###	
	frontLum = robot.getFrontLuminosity()
	backLum = robot.getBackLuminosity()
	print("front lum : ", frontLum)
	print("back lum : ", backLum)

	lumThreshold = 70
	
	if(frontLum >= lumThreshold and backLum >=lumThreshold):
		#VERT, OVA est sur la ligne
		robot.setLedColor(0, 255, 0)
		print("Est sur la ligne")
	elif(frontLum <= lumThreshold and backLum <= lumThreshold):
		robot.setLedColor(255, 0, 0)
		print("N'est pas sur la ligne")
		explodeSong = [(880, 1000)]
		robot.playMelody(explodeSong)
	elif(frontLum <= lumThreshold or backLum <=lumThreshold):
		#BLEU, OVA est à moitié sur la ligne
		robot.setLedColor(0, 0, 255)
		print("Est à moitié sur la ligne")
		touchedLineSong = [(440, 500), (110, 500)]
		robot.playMelody(touchedLineSong)
	robot.update()

	######
	
	

pygame.quit()
robot.stop()
robot.update()

