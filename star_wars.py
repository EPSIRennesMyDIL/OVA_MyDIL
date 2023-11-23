
from j2l.pyrobotx.robot import IRobot, RobotEvent
import j2l.pyrobotx.client as ova

import os
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

### NOTES DE MUSIQUE ###
c = 261
d = 294
e = 329
f = 349
g = 391
gS = 415
a = 440
aS = 455
b = 466
cH = 523
cSH = 554
dH = 587
dSH = 622
eH = 659
fH = 698
fSH = 740
gH = 784
gSH = 830
aH = 880

########################
###### STAR WARS #######
premierCouplet = [
  (a, 500),
  (a, 500),    
  (a, 500),
  (f, 350),
  (cH, 150),  
  (a, 500),
  (f, 350),
  (cH, 150),
  (a, 650),
  (0, 500),

  (eH, 500),
  (eH, 500),
  (eH, 500) , 
  (fH, 350),
  (cH, 150),
  (gS, 500),
  (f, 350),
  (cH, 150),
  (a, 650)]


robot.playMelody(premierCouplet)
robot.update()

time.sleep(5)
print("########################")
print("🔴 TERMINE")

robot.stop()
robot.update()

