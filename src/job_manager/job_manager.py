#!/usr/bin/python3
################################################################################
################################################################################
###   ##  ### ### ###     ### # # ### # # ### # # ###   ########################
###   # # #   #   # #      #  # # # # # # #   # #  #    ########################
###   # # ##  ##  ##       #  ### # # # # # # ###  #    ########################
###   # # #   #   #   # #  #  # # # # # # # # # #  #    ########################
###   ##  ### ### #   ###  #  # # ### ### ### # #  #    ########################
################################################################################
################################################################################
## Author : Jormungandr                                                       ##
################################################################################
## This script runs and manages jobs on the cluster. It should be run on      ##
## restart as a cronjob and can be queried/interacted with via the named      ##
## pipes in the communication folder.                                         ##
################################################################################
################################################################################
import sys
import os
import time
import math
import threading
import subprocess


def run():
	while True:
		check_pipe() # Check for incoming


def check_pipe():
	in_pipe = os.open("../../communication/man_in", os.O_RDONLY)
	in_pipe = os.fdopen(in_pipe)
	text = in_pipe.read()
	#print("TEXT ABOVE:\n{}\nTEXT BENEATH".format(text))
	data = text.split("\n")
	h_val = data[0]
	command = data[1]
	print("Hash: {0}\nCommand: {1}".format(h_val,command))
	check_command(command,data)

def check_command(command, data):
	pass


if __name__ == "__main__":
	run()
