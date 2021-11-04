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
from job import Job


def run():
	while True:
		check_pipe() # Check for incoming


def check_pipe():
	# Get data
	in_pipe = os.open(man_in, os.O_RDONLY)
	in_pipe = os.fdopen(in_pipe)
	text = in_pipe.read()
	os.close(in_pipe)
	# Format data
	info = text.split("#"*80)
	headers = info[0].split("\n")
	h_val = headers[0]
	command = headers[1]
	args = info[1].split("\n")
	data = info[2]
	print("Hash: {0}\nCommand: {1}".format(h_val,command))
	check_command(h_val,command,args,data)

def check_command(h_val, command, args, data):
	# Hella if statements
	if command == "show_queue":
		pass
	elif command == "add_job":
		pass
	elif command == "cluster_info":
		if args[0] == "quick":
			pass
		elif args[0] == "detailed":
			pass
	elif command == "incorrect_recipient":
		send(h_val,  data)
	else:
		pass


def send(h_val, data):
	out_pipe = os.open(man_out, os.O_WRONLY)
	out_pipe = os.open(out_pipe)
	response = "{0}\n{1}".format(h_val,data)
	out_pipe.write(response)
	os.close(out_pipe)


def get_status(h_val, args, data):
	pass


jobs = []
nodes = []
temperatures = []
past_jobs = []
man_in = "../../communications/man_in"
man_out = "../../communications/man_out"

if __name__ == "__main__":
	run()
