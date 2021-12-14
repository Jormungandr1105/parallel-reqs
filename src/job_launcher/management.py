
class Management():

	def __init__(self, addresses):
		self.addresses = addresses

	def power_on(self):
		power = ""
		for x in self.addresses:
			if x == "1":
				power += "1"
			else:
				power += "0"
		
	def power_off(self):
		power = ""
		for _ in self.addresses:
			power += "0"

	def throw_error(self):
		self.set_color("error")
		self.power_off()

	def exit_success(self):
		self.set_color("success")

	def timeout(self):
		self.set_color("timeout")
		self.power_off()

	def set_temp(self, temperature):
		pass

	def set_color(self, color):
		pass
