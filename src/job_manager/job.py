# Struct that Stores Job Data
import os
import time
import math
import threading
import subprocess
import sys



class Job():
	### CLASS VARIABLES


	### INIT
	def __init__(self, id, start_time, end_time, data):
		# id is an hex code assigned to the job
		# start_time is a float of time in seconds since the Epoch
		self.id = id
		self.start_time = start_time
		self.end_time = end_time
		self.thread = None
		self.path = data[0]
		self.name = data[1]
		self.file = data[2]
		self.hostfile = data[4]
		self.num_nodes = data[5]
		self.percent_complete = 0
		self.finished = False
		self.process = None
		self.output = []

	### GETTERS
	def get_id(self):
		return self.id
		
	def get_data(self, level):
		start_date = time.ctime(self.start_time)
		t_elapsed = time.time() - self.start_time
		days = math.floor(t_elapsed/86400)
		hours = math.floor((t_elapsed-days*86400)/3600)
		minutes = math.floor((t_elapsed-days*86400-hours*3600)/60)
		seconds = math.floor(t_elapsed-days*86400-hours*3600-minutes*60)
		if level == "basic":
			string = "| {:16s} |".format(self.name)
			string += " {0:03d}:{1:02d}:{2:02d}:{3:02d} |".format(days,hours,minutes,seconds)
			string += " {:02d} |".format(self.percent_complete)
			return string
		elif level == "deep":
			pass

	def get_end_time(self):
		return self.end_time

	def get_pipes(self):
		return self.in_pipe, self.out_pipe

	### SETTERS
	def set_end_time(self, end_time):
		# end_time is a float of time in seconds since the Epoch
		self.end_time = end_time

	def set_pipes(self, in_pipe, out_pipe):
		self.in_pipe = in_pipe
		self.out_pipe = out_pipe

	### RUN
	def run(self):
		exec_file = os.path.join(self.path,self.file)
		execute = "mpiexec%-n%{0}%--hostfile%{1}%".format(self.num_nodes, os.path.join(self.path,self.hostfile))
		try:
			ext_begin = exec_file.rfind(".")
			if exec_file[ext_begin:] == ".py":
				execute += "python3%-m%mpi4py%{0}".format(exec_file)
			else:
				execute += "{0}".format(exec_file)
		except ValueError:
			execute += "{0}".format(exec_file)
		finally:
			print(os.getcwd())
			#execute += "%>%../pipe"
			args = execute.split("%")
			#print(args)
			self.process = subprocess.Popen(args,bufsize=1,universal_newlines=True,stdout=subprocess.PIPE)
			#output_proc = threading.Thread(target=self.collect_output)
			#output_proc.start()
			'''
			while self.process.poll() is None and len(self.output) != 0:
				if len(self.output) != 0:
					out = self.output.pop(0)
					if out[0] == "%":
						self.percent_complete = int(out[1:])
					else:
						print(out)
					time.sleep(1)
					print("Loop")
			print("END LOOP")
			'''
			'''
			while True:
				output = self.process.stdout.readline()
				if self.process.poll() is not None:
					break
				if output:
					print(output,end="")
			'''
			while self.process.poll() is None:
				out = self.process.stdout.read(1)
				if out == "":
					break
				else:
					sys.stdout.write(out)
					sys.stdout.flush()
			self.process.wait()
		if self.process.returncode == 0:
			print("PROCESS COMPLETED SUCCESSFULLY")
			self.finished=True
		elif self.process.returncode == 1:
			print("SYSTEM ENCOUNTERED AN ERROR")
		return

	def collect_output(self):
		print(os.getcwd())
		while self.process.poll() is None:
			print("Entered loop")
			in_pipe = os.open("../pipe", os.O_RDONLY)
			in_pipe = os.fdopen(in_pipe)
			text = in_pipe.read()
			#if text[0] == "%":
				#self.percent_complete = int(text[1:])
			#else:
			print("Received from PIPE: {}".format(text))

	def kill(self):
		if not self.finished:
			if self.process.poll() is not None:
				self.process.kill()
			self.finished=True


if __name__ == "__main__":
	cs_time = time.time()
	print(cs_time)
	c_time = time.ctime(cs_time)
	print(c_time)
