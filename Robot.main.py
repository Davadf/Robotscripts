from gpiozero import Robot, Button
from signal import pause
from signal import pause

from gpiozero import Robot, Button

#motor1 = Motor(, )
#motor2 = Motor(, )


# Motor pin config
robot = Robot(left=(4, 14), right=(17, 18))

# Button config
left = Button(26)
right = Button(16)
fw = Button(21)
bw = Button(20)

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

pause()
