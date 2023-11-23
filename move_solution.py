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
	
	"""if(keyQ[pygame.K_DOWN] - keyQ[pygame.K_UP]) == -1:
		avance(robot)
	elif keyQ[pygame.K_DOWN] - keyQ[pygame.K_UP] == 1:
		recule(robot)
	if keyQ[pygame.K_RIGHT] - keyQ[pygame.K_LEFT] == 1:
		droite(robot)
	elif keyQ[pygame.K_RIGHT] - keyQ[pygame.K_LEFT] == -1:
		gauche(robot)
	elif [keyQ[pygame.K_DOWN], keyQ[pygame.K_UP], keyQ[pygame.K_RIGHT], keyQ[pygame.K_LEFT]] == [0,0,0,0]:
		stop(robot)"""
	
	frontLum = robot.getFrontLuminosity()
	backLum = robot.getBackLuminosity()
	print("front lum : ", frontLum)
	print("back lum : ", backLum)

	luminosity = 70

	
	if(frontLum >= luminosity and backLum >=luminosity):
		#VERT, OVA est sur la ligne
		robot.setLedColor(0, 255, 0)
		print("sur la ligne")
	elif(frontLum <= luminosity and backLum <=luminosity):
		robot.setLedColor(255, 0, 0)
		print("pas sur la ligne")
		explode = [(880, 1000)]
		robot.playMelody(explode)
	elif(frontLum <= luminosity or backLum <=luminosity):
		#BLEU, OVA est à moitié sur la ligne
		robot.setLedColor(0, 0, 255)
		print("a moitie sur la ligne")
		touchedLine = [(440, 500), (110, 500)]
		robot.playMelody(touchedLine)
	robot.update()
	""""
	robot.enableCamera(True)
	
	robot.update()
	sr = 0
	sg = 0
	sb = 0
	n = 0
	w = robot.getImageWidth()
	h = robot.getImageHeight()
	for x in range(0, w, 10):
		for y in range(0, h, 10):
			color = robot.getImagePixelRGB(x, y)
			sr += color[0]
			sg += color[1]
			sb += color[2]
			n += 1
	if (n > 0):
		sr = sr // n
		sg = sg // n
		sb = sb // n
		print("📸 Camera img " + str(w) + "x" + str(h) + " shot after " +
			str(robot.getImageTimestamp()) + "ms")
		print("🔴<R>=" + str(sr) + " 🟢<G>=" + str(sg) + " 🔵<B>=" + str(sb))
		robot.setLedColor(sr, sg, sb)

	print("Face detection")
	face_cascade = cv2.CascadeClassifier('face_detector.xml')
	img = cv2.imread('img.jpeg')
	faces = face_cascade.detectMultiScale(img, 1.1, 4)
	for (x, y, w, h) in faces :
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
		cv2.imwrite("img.jpeg", img)
	print('Enregistré avec succès')

	robot.update()

	#if compteur >= 50:
	image = pygame.image.load("img.jpeg").convert_alpha()
	window.blit(image, (0,0))
	pygame.display.flip()
	compteur = 0
	compteur +=1"""

	

pygame.quit()
robot.stop()
robot.update()

