#/usr/bin/python3
import time
import os
from ArduinoController import *


def boot_system():
	global controller
	controller = ArduinoController()


def await_orders():
	for _ in range(10): # Temp while testing, will become while(True):
		first_file = ""
		first_num = 1000000000000
		directory = os.listdir(command_path)
		for file in directory:
			if file != "template.cmnd":
				file_no = int(file.split(".")[0])
				if file_no < first_num:
					first_num = file_no
					first_file = file
		if first_file != "":
			f = open(command_path+"/"+file)
			text = f.read()
			execute_orders(text)
			f.close()
			os.remove(command_path+"/"+file)
		time.sleep(2)


def execute_orders(order):
	# Parse order
	order_data = order.split(":")
	order_key = order_data[0]
	order_value = order_data[1].split("\n")[0]
	if order_key == "POWER":
		vals = []
		for x in order_value:
			vals += int(x)
		controller.power_control(vals)
	elif order_key == "LED":
		if len(order_value) == 6:
			# send hex code
			controller.change_color_hex(order_value)
		else:
			# send color from list
			controller.change_color(str(order_value))
	elif order_key == "FANS":
		pass
		


command_path = "../commands"
controller = None

if __name__ == '__main__':
	boot_system()
	await_orders()
	