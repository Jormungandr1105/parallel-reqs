import serial
import sys
import time

class ArduinoController():
	'''
		Coordinates the various functionalities of the hardware aspect of the cluster
	'''
	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
		time.sleep(2)

	def change_color(self, color_index):
		self.ser.write(b'C'+colors[color_index])
		time.sleep(2)

	def change_color_hex(self, color_hex):
		self.ser.write(b'C'+bytes(color_hex.lower(),'utf-8'))
		time.sleep(2)

	def continuous_change_color(self):
		while True:
			for color in cont_colors:
				self.ser.write(color)
				time.sleep(2)

	def power_control(self, nodes_array):
		contact = b'P'
		for i in nodes_array:
			if i == 0:
				contact += b'0'
			else:
				contact += b'1'
		self.ser.write(contact)
		time.sleep(2)


cont_colors = [b'ff0000',b'ffff00',b'00ff00',b'00ffff',b'0000ff',b'ff00ff']
colors = [b'ffffff',b'ff0000',b'00ff00',b'0000ff',b'ff00ff',b'ffff00',b'000000']
#colors = ["White_0", "Red_1", "Green_2", "Blue_3", "Purple_4", "Yellow_5", "Off_6"]

if __name__ == '__main__':
	# BASIC SETUP
	controls = ArduinoController()
	controls.change_color(int(sys.argv[1]))
	#time.sleep(5)
	#controls.continuous_change_color()
	controls.power_control([0,0,0,0])