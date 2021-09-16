import sys
import os


def run_job():
	pass


def load_config(filename):
	text = read_file(filename)
	options = text.split("\n")
	for option in options:
		if option != "":
			option_key = option.split(":")[0].strip("#").strip(" ")
			option_value = option.split(":")[1].strip(" ")
			set_option(option_key, option_value)


def set_option(option_key, option_value):
	global keys
	global values
	for i in range(keys):
		if option_key == keys[i]:
			values[i] = option_value
			return
	return


def read_file(filename):
	f = open(filename, "r")
	text = f.read()
	f.close()
	return text


keys = ["JOB_NAME", "JOB_FILE", "NUM_NODES", "HOST_LIST", "MAX_TIME", "COUNT_TIME"]
values = ["DEFAULT_JOB", "roll_call.py", 0, os.curdir+"machinefile", "00:00:00:00", False]


if __name__ == '__main__':
	assert(len(sys.argv) == 2)
	load_config(sys.argv[1])
	run_job()
