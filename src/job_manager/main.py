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
from job_manager.job import Job
from job_manager.queue import Queue
#from job import Job
#from queue import Queue



def main_loop():
	current_queue = Queue()
	past_queue = Queue()
	
	while True:
		check_pipe(current_queue, past_queue) # Check for incoming


def check_pipe(current_queue, past_queue):
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
	check_command(h_val,command,args,data,current_queue,past_queue)


def check_command(h_val, command, args, data, current_queue, past_queue):
	# Hella if statements
	if command == "show_queue":
		data = get_queue(current_queue,args)
		send(h_val, data)
	elif command == "add_job":
		data = add_job()
	elif command == "cluster_info":
		pass
	elif command == "incorrect_recipient":
		send(h_val, data)
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


def get_queue(current_queue,args):
	data = ""
	jobs = current_queue.get_jobs()
	for job in jobs:
		data += "{}\n".format(job.get_data(args[0]))
	return data


def add_job(h_val,data,current_queue):
	job_params = data.split("\n")
	curr_time = time.time() + offset
	run_time = convert_to_seconds(data[4])
	new_job = Job(h_val,curr_time,curr_time+run_time)
	current_queue.add_jobs(new_job)


def convert_to_seconds(time):
	t_s = 0
	time_data = time.split(":")
	t_s += int(time_data[3])
	t_s += int(time_data[2])*60
	t_s += int(time_data[1])*3600
	t_s += int(time_data[0])*86400
	return t_s


man_in = "../../communications/man_in"
man_out = "../../communications/man_out"
offset = 2


if __name__ == "__main__":
	main_loop()
