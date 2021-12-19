import os
import sys
import secrets

class API():
	def __init__(self):
		self.path = os.path.dirname(__file__)+"/../../communication/"

	def generate_hash(self):
		return secrets.token_hex(4)

	def send_request(self, data):
		while True: # Setting Up For Return Fifo
			hash = self.generate_hash()
			if not (os.path.isfile(self.path+str(hash))):
				break
		os.mkfifo(self.path+str(hash)) # Reply fifo taken care of
		# Actually make request here
		spacer = "#"*80+"\n"
		request = "{0}\n{1}\n".format(str(hash),data[0])
		request += spacer
		for arg in data[1]:
			request += arg + "\n"
		request += spacer
		for data_line in data[2]:
			request += data_line + "\n"
		request += spacer
		#print(request)
		out_pipe = os.open(self.path+"man_in", os.O_WRONLY)
		out_pipe = os.fdopen(out_pipe, "w")
		out_pipe.write(request)
		return hash

	def await_reply(self, hash):
		in_pipe = os.open(self.path+str(hash), os.O_RDONLY)
		in_pipe = os.fdopen(in_pipe)
		reply = in_pipe.read()
		try:
			os.remove(self.path+str(hash)) # Clean Up Mess
		except FileNotFoundError:
			reply = "No Response\n"
		return reply

	def add_job(self, job_info):
		data = ["add_job",job_info[0],job_info[1]]
		hash = self.send_request(data)
		reply = self.await_reply(hash)
		return reply

	def show_queue(self):
		data = ["show_queue","\n","\n"]
		hash = self.send_request(data)
		reply = self.await_reply(hash)
		return reply


def parse_data(data):
	return data


if __name__ == "__main__":
	api = API()
	command = sys.argv[1]
	if len(sys.argv) > 2:
		data = sys.argv[2]
	if command == "show_queue":
		print(api.show_queue())
	elif command == "add_job":
		print(api.add_job(parse_data(data)))

