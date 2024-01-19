from j2l.pyrobotx.robot import IRobot, RobotEvent
import j2l.pyrobotx.client as ova
import cv2

import os
os.system("pip install requests")
import random
import time

from deplacement import *

# Pour piloter une ova sur un LAN ou si vous êtes directement connecté à son point d'accès
robot:IRobot = ova.OvaClientHttpV2(url="192.168.71.1") 

# Appel de la callback onRobotEvent pour chaque évènements du robot
def onRobotEvent(source, event, value):
	print("Rx event", event, "from", source, ":", value)

robot.addEventListener(RobotEvent.imageReceived, onRobotEvent)
robot.addEventListener(RobotEvent.robotChanged, onRobotEvent)
robot.addEventListener(RobotEvent.robotConnected, onRobotEvent)
robot.addEventListener(RobotEvent.robotDisconnected, onRobotEvent)

print("########################")
while (robot.isConnectedToRobot() == False):
	print("Awaiting robot connection...")
	robot.update()
	time.sleep(1)
"""
robot.setMotorSpeed(0,0,0)
robot.update()
animation = [[-100,100,8],
			 [100,100,2]]
while(True) :
	robot.setMotorAnimation(animation)
	robot.update()

while(True) :
	avance(robot, duree=8)
	droite(robot, duree = 2)"""
	
robot.stop()
robot.update()
"""
import keyboard
while True:
    if keyboard.is_pressed("a"):
        print("You pressed 'a'.")"""
        

print("########################")
print("📸 Test camera")
robot.enableCamera(True)
for i in range(50):
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
	face_cascade = cv2.CascadeClassifier('ia/face_detector.xml')
	img = cv2.imread('img.jpeg')
	faces = face_cascade.detectMultiScale(img, 1.1, 4)
	for (x, y, w, h) in faces :
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
		cv2.imwrite("img.jpeg", img)
	print('Enregistré avec succès')
	time.sleep(0.1)
robot.enableCamera(False)

print("########################")
print("🔴 END TEST")
endMelody = []
for i in range(10, 2, -1):
	endMelody.append((i, 50))
robot.playMelody(endMelody)
robot.stop()
robot.update()

