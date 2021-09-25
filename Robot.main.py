# My program for my Robot with Light, Buzzer, and later sensors
# Made by David github: Davadf

from time import sleep

from gpiozero import Buzzer
from gpiozero import DistanceSensor
from gpiozero import LED
from gpiozero import Robot, Button

# motor1 = Motor(, )
# motor2 = Motor(, )

# buzzer config
buzzer = Buzzer(18)

# Led config
led = LED(17)

# sensor config
sensor = DistanceSensor(echo=10, trigger=11, threshold_distance=0.1)

# Motor pin config
robot = Robot(left=(4, 14), right=(17, 18))

# Button config
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

# sensor
while True:
    print(sensor)
    sensor.wait_for_in_range(robot.right())
    print('collision incomming')

# Led control
right.when_pressed = led.on()
right.when_released = led.off()
left.when_pressed = led.on()
left.when_released = led.off()
fw.when_pressed = led.on()
fw.when_released = led.off()

pause()
