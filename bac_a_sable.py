from j2l.pyrobotx.robot import IRobot, RobotEvent
import j2l.pyrobotx.client as ova
import cv2

import os
#os.system("pip install requests")
import random
import time

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

print("########################")
print("🟢 BEGIN TEST")
robot.enableCamera(False)
beginMelody = [
	(440, 500),
	(880, 500),
	(220, 500),
	(110, 500)
]

robot.playMelody(beginMelody)
robot.setMotorSpeed(0, 0)
robot.setLedColor(0, 0, 0)
robot.update()

print("########################")
print("🔴 END TEST")
endMelody = []
for i in range(10, 2, -1):
	endMelody.append((i, 50))
robot.playMelody(endMelody)
robot.stop()
robot.update()

