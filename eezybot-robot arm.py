import pygame

from adafruit_servokit import ServoKit
servo_controller = ServoKit(channels=16)

import time

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print (joysticks)


if len(joysticks) == 0:
	print("No joystick connected")
	exit(1)


# make j be the first item from the joysticks list
j = joysticks[0]

j.get_name()

j.init()

print (j.get_name())

print(j.get_button(0))



def print_buttons(js):
	pygame.event.pump()
	for button_num in range(js.get_numbuttons()):
		print("Button {} is pressed ? {}".format(button_num, js.get_button(button_num)))


def print_axes(js):
	pygame.event.pump()
	for axis_num in range(js.get_numaxes()):
		print("axis {} is pressed ? {}".format(axis_num, js.get_axis(axis_num)))



# ensure x is between 0 and 180
def servo_clamp(x):
	if x > 180:
		return 180
	if x < 0:
		return 0
	return x


#while True:
#	print_buttons(j)
#	print_axes(j)
#	print("-------------------------------------------------------------------------------------")
#	time.sleep(1)


#RT is Axis 5, minimum value is (-1.0) (minimum means button not clicked) 
#(when Axis is pressed all the way it is (.999969482421875)) 
# the numbers go from (-1 to +1)

gripper_servo = servo_controller.servo[1]
base_servo = servo_controller.servo[3]
shoulder_servo = servo_controller.servo[2]
elbow_servo = servo_controller.servo[4]


#gripper_closed_value = 0
#gripper_open_value = 150


while True:
	pygame.event.pump()
	
	# Gripper control!
	rt = j.get_axis(5)
	#gripper_servo.angle = rt * (gripper_closed_value - gripper_open_value) / 2 + (2*gripper_open_value - gripper_closed_value)
	gripper_servo.angle = servo_clamp( (-150/2) * rt + (150/2) )
	
	# Base Control!
	r3leftright = j.get_axis(3)
	base_servo.angle = 90*r3leftright+90 
	
	# Shoulder control!
	r3updown = j.get_axis(4)
	# shoulder_servo.angle = 45.5*r3updown+87.5 # oops, this one is backwards. when the stick is up, the reading is -1 which is wierd
	shoulder_servo.angle = -45.5*r3updown + 87.5
	
	# Elbow control!
	l3updown = j.get_axis(1)
	elbow_servo.angle = 34.5*l3updown+144.5
	
	
	
	
	
	
	
	
	
	
