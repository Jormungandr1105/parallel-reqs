import sys
import os
import time
import threading
import subprocess
from management import Management


def launch_job():
	max_time = get_seconds(values[4])
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
		print("PROCESS KILLED: TIME LIMIT EXCEEDED\nTOTAL TIME PASSED: {}".format(t_tot))
		Manager.timeout()
	else:
		print("TOTAL TIME PASSED: {0}".format(t_tot))


def run_job():
	exec_file = values[1]
	execute = "mpiexec -np {0} --hostfile {1} ".format(values[2], values[3])
	try:
		ext_begin = exec_file.rfind(".")
		if exec_file[ext_begin:] == ".py":
			execute += "python3 -m {0}".format(values[1])
		else:
			execute += "{0}".format(values[1])
	except ValueError:
		execute += "{0}".format(values[1])
	finally:
		status = subprocess.run(execute, capture_output=True)
	if status.returncode == 0:
		print("PROCESS COMPLETED SUCCESSFULLY")
	elif status.returncode == 1:
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
	text = read_file(values[3])
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
	global keys
	global values
	for i in range(len(keys)):
		if option_key == keys[i]:
			values[i] = option_value
			return
	return


def read_file(filename):
	# Easy read, closes as early as possible
	f = open(filename, "r")
	text = f.read()
	f.close()
	return text


Manager = None
keys = ["JOB_NAME", "JOB_FILE", "NUM_NODES", "HOST_LIST", "MAX_TIME", "COUNT_TIME"]
values = ["DEFAULT_JOB", None, 0, os.curdir+"machinefile", "000:00:00:00", False]


if __name__ == '__main__':
	assert(len(sys.argv) == 2)
	load_config(sys.argv[1])
	boot_system()
	launch_job()
