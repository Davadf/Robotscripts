# My program for my Robot with Light, Buzzer, and later sensors
# Made by David github: Davadf
# TODO My code music https://www.youtube.com/watch?v=fJoOAbyMQG8&ab_channel=Blake
# TODO https://open.spotify.com/playlist/37i9dQZF1E4vQNrG1vfweo

from time import sleep
from gpiozero import LightSensor
from gpiozero import Buzzer
from gpiozero import DistanceSensor
from gpiozero import LED
from gpiozero import Robot, Button
from gpiozero import Servo

# motor1 = Motor(, )
# motor2 = Motor(, )

# TODO Objekt detection integration
# TODO INFO https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi

# buzzer config
buzzer = Buzzer(18)

# Led config
led = LED(17)
lamp = LED(18)

# sensor config
sensor = DistanceSensor(echo=10, trigger=11, threshold_distance=0.1)

# light sensor config
ldr = LightSensor(18)

# Motor pin config
robot = Robot(left=(4, 14), right=(17, 18))

# Button config
# TODO Find real and right buttons for control
left = Button(26)
right = Button(16)
fw = Button(21)
bw = Button(20)
bz = Button(27)

print('Made by David')

# forward
fw.when_pressed = robot.forward
fw.when_released = robot.stop

# left
left.when_pressed = robot.left
left.when_released = robot.stop

# right
right.when_pressed = robot.right
right.when_released = robot.stop

# backward
bw.when_pressed = robot.backward
bw.when_released = robot.stop

# buzzer
bz.when_held = buzzer.on()
sleep(1)
buzzer.off()
sleep(1)

# TODO Change buzzer for Cat miau
# TODO Cat miau file ‪C:\Users\David\Desktop\Robot scripts\catr.mp3

# cam control

 # TODO Build control with keys or even mouse to rotate the cam
 # TODO Use servos to lean cam
 # Info https://gpiozero.readthedocs.io/en/stable/api_output.html#servo
 # Note Watch out for overtotation of servos and right config

# light sensor
ldr.wait_for_dark()
lamp.on()

    # TODO Checke for daytime to prove if its night or day

# sensor
while True:
    print(sensor)
    sensor.wait_for_in_range(robot.right())
    print('collision incomming')

    # TODO Use objekt detection to see if person in near

# Led control
right.when_pressed = led.on()
right.when_released = led.off()
left.when_pressed = led.on()
left.when_released = led.off()
fw.when_pressed = led.on()
fw.when_released = led.off()

pause()

# TODO Baue vieleicht noch ein rachensystem durch erkannte zahlen oder Finger ein