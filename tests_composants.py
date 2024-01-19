from j2l.pyrobotx.robot import IRobot, RobotEvent
import j2l.pyrobotx.client as ova
import cv2

import os

import random
import time
#os.system("pip install requests")
"""
# Pour piloter une ova via un broker MQTT
robot: IRobot = ova.OvaClientMqtt(server="mqtt.jusdeliens.com",
                                  port=1883,
                                  useProxy=False)
"""
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


for i in range(3, 11, 1):
	beginMelody.append((i, 50))
robot.playMelody(beginMelody)
robot.setMotorSpeed(0, 0)
robot.setLedColor(0, 0, 0)
robot.update()

print("########################")
print("🔦 Test sensors")
print("Change the light above the robot to see how sensors values change")
for i in range(50):
	robot.update()
	time.sleep(0.1)
	print("⬆️ Photo front lum: ", robot.getFrontLuminosity())
	print("⬇️ Photo back lum: ", robot.getBackLuminosity())
	print("🔋 Battery voltage: ", robot.getBatteryVoltage())
	print("⏱️ Timestamp: ", robot.getTimestamp())
	print("📸 Camera img " + str(robot.getImageWidth()) + "x" +
	      str(robot.getImageHeight()) + " shot after " +
	      str(robot.getImageTimestamp()) + "ms")

print("########################")
print("🔊 Test actuators")
robot.stop()
for i in range(20):
	robot.update()
	robot.setLedColor(random.randint(0, 255), random.randint(0, 255),
	                  random.randint(0, 255))
	robot.playMelody([[random.randint(0, 12), 200]])
	robot.setMotorSpeed(random.randint(0, 50), random.randint(0, 50))
robot.stop()

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

