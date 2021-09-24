import sys
import os
import time
import math
import threading
import subprocess
from management import Management


def launch_job():
	global args
	max_time = get_seconds(args["MAX_TIME"])
	# Create thread
	t_main = threading.Thread(target=run_job, daemon=True)
	# Hit the clock
	start_time = time.time()
	# Start program
	t_main.start()
	# Watch the clock
	while(time.time()-start_time < max_time and t_main.is_alive()):
		time.sleep(1)
	# Clean Up
	t_tot = time.time() - start_time
	if (t_tot >= max_time):
		print("PROCESS KILLED: TIME LIMIT EXCEEDED\nTOTAL TIME PASSED: {}".format(math.floor(t_tot)))
		Manager.timeout()
	else:
		print("TOTAL TIME PASSED: {0}".format(math.floor(t_tot)))


def run_job():
	global job
	global args
	exec_file = args["JOB_FILE"]
	execute = "mpiexec -np {0} --hostfile {1} ".format(args["NUM_NODES"], args["HOST_LIST"])
	try:
		ext_begin = exec_file.rfind(".")
		if exec_file[ext_begin:] == ".py":
			execute += "python3 {0}".format(exec_file)
		else:
			execute += "{0}".format(exec_file)
	except ValueError:
		execute += "{0}".format(exec_file)
	finally:
		arguments = execute.split(" ")
		#job = subprocess.Popen(args, stdout=subprocess.PIPE, bufsize=1)
		job = subprocess.run(arguments, capture_output=True)
		save_file("out.txt", job.stdout.decode("utf-8"))
		save_file("error.log", job.stderr.decode("utf-8"))
		#while job.poll() != None:

	if job.returncode == 0:
		print("PROCESS COMPLETED SUCCESSFULLY")
	elif job.returncode == 1:
		print("SYSTEM ENCOUNTERED AN ERROR")
	return


def boot_system():
	# Sets up the hardware manager
	global Manager
	addresses = get_addresses()
	Manager = Management(addresses)
	Manager.power_on()
	#time.sleep(7)
	return


def get_addresses():
	# Figures out which nodes are to be used
	node_nums = []
	text = read_file(args["HOST_LIST"])
	nodes = text.split("\n")
	for node in nodes:
		node_number = node.split(":")[0].strip("node")
		node_nums.append(node_number)
	return node_nums


def get_seconds(string_time):
	# Calculates the number of seconds that the job should be allowed to run for
	array_time = string_time.split(":")
	seconds = int(array_time[3])
	seconds += int(array_time[2])*60
	seconds += int(array_time[1])*3600
	seconds += int(array_time[0])*86400
	return seconds


def load_config(filename):
	# Reads through the config file and sets up an appropriate job
	text = read_file(filename)
	options = text.split("\n")
	for option in options[1:]:
		if option != "":
			option_key = option.split(":")[0].strip("#").strip(" ")
			option_value_array = option.split(":")[1:]
			option_value = ""
			for option_value_part in option_value_array:
				option_value += ":" + option_value_part.strip(" ")
			option_value = option_value.strip(":")
			print("{0} -> {1}".format(option_key, option_value))
			set_option(option_key, option_value)


def set_option(option_key, option_value):
	# Figures out what the configs are trying to set, and then does it
	global args

	if option_key in args:
		args[option_key] = option_value
	return


def read_file(filename):
	# Easy read, closes as early as possible
	f = open(filename, "r")
	text = f.read()
	f.close()
	return text


def save_file(filename, text):
	# Easy Write
	f = open(filename, "w+")
	f.write(text)
	f.close()


Manager = None
keys = ["JOB_NAME", "JOB_FILE", "NUM_NODES", "HOST_LIST", "MAX_TIME", "COUNT_TIME", "SAVE_FILE"]
values = ["DEFAULT_JOB", None, 0, os.curdir+"/machinefile", "000:00:00:00", False, "out.txt"]
args = {
	"JOB_NAME": "DEFAULT JOB",
	"JOB_FILE": None,
	"NUM_NODES": 0,
	"HOST_LIST": os.curdir+"/machinefile",
	"MAX_TIME": "000:00:00:00",
	"SAVE_FILE": "out.txt"
}

if __name__ == '__main__':
	assert(len(sys.argv) == 2)
	load_config(sys.argv[1])
	boot_system()
	print(args)
	launch_job()
