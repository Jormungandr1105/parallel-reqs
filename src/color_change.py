#!/usr/bin/python3
import serial
import sys
import time


def change_color(color_index):
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
	msg = ser.readline()
	#print(msg)
	ser.write(colors[color_index])

def continuous_change_color():
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
	msg = ser.readline()
	while True:
		for color in cont_colors:
			ser.write(color)
			time.sleep(2)

cont_colors = [b'ff0000',b'ffff00',b'00ff00',b'00ffff',b'0000ff',b'ff00ff']
colors = [b'ffffff',b'ff0000',b'00ff00',b'0000ff',b'ff00ff',b'ffff00',b'000000']
#colors = ["White_0", "Red_1", "Green_2", "Blue_3", "Purple_4", "Yellow_5", "Off_6"]

if __name__ == '__main__':
	# BASIC SETUP
	change_color(int(sys.argv[1]))