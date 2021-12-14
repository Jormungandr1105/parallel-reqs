# Simple program to test the website's ability to update itself
import time
import json
import math as m


def run():
	n = 0
	n_max = 100
	while( n < n_max):
		tick(n, n_max)
		f = open("file.json", "w+")
		f.write(json.dumps(j_object, indent=2))
		f.close()
		time.sleep(1)
		n = n+1

def tick(n, n_max):
	global j_object
	## Simulate jobs
	##############################################################################
	# Job 1
	min1 = 0
	max1 = n_max-1
	if n == min1:
		job_01 = {}
		job_01["job"] = "job01"
		job_01["percent"] = 0
		j_object["progress"].append(job_01)
		# Spin Up Cores
		j_object["nodes"][0]["cores"] += 2
		j_object["nodes"][1]["cores"] += 1
		j_object["nodes"][2]["cores"] += 1
		j_object["nodes"][3]["cores"] += 1
		j_object["progress"][0]["job"] = "Job_01: LEVIATHAN"
	if n == max1:
		j_object["nodes"][0]["cores"] -= 2
		j_object["nodes"][1]["cores"] -= 1
		j_object["nodes"][2]["cores"] -= 1
		j_object["nodes"][3]["cores"] -= 1
	if n >= min1:
		j_object["progress"][0]["percent"] = int(min(100, 100*float((n-min1)/(max1-min1))))
	##############################################################################
	# Job 2
	min2 = m.floor(n_max/3)
	max2 = m.floor(2*n_max/3)
	if n == min2:
		job_02 = {}
		job_02["job"] = "job02"
		job_02["percent"] = 0
		j_object["progress"].append(job_02)
		# Spin Up Cores
		j_object["nodes"][1]["cores"] += 2
		j_object["nodes"][2]["cores"] += 2
		j_object["nodes"][3]["cores"] += 2
		j_object["nodes"][4]["cores"] += 2
		j_object["nodes"][5]["cores"] += 2
		j_object["nodes"][6]["cores"] += 2
		j_object["progress"][1]["job"] = "Job_02: PRIMES"
	if n == max2:
		j_object["nodes"][1]["cores"] -= 2
		j_object["nodes"][2]["cores"] -= 2
		j_object["nodes"][3]["cores"] -= 2
		j_object["nodes"][4]["cores"] -= 2
		j_object["nodes"][5]["cores"] -= 2
		j_object["nodes"][6]["cores"] -= 2
	if n >= min2:
		j_object["progress"][1]["percent"] = int(min(100, max(100*float((n-min2)/(max2-min2)),0)))
	##############################################################################
	# Job 3
	min3 = m.floor(n_max/2)
	max3 = n_max-1
	if n == min3:
		job_03 = {}
		job_03["job"] = "job03"
		job_03["percent"] = 0
		j_object["progress"].append(job_03)
		# Spin Up Cores
		j_object["nodes"][4]["cores"] += 4
		j_object["nodes"][5]["cores"] += 4
		j_object["nodes"][6]["cores"] += 4
		j_object["progress"][2]["job"] = "Job_03: PROJECT_DOGE"
	if n == max3:
		j_object["nodes"][4]["cores"] -= 4
		j_object["nodes"][5]["cores"] -= 4
		j_object["nodes"][6]["cores"] -= 4
	if n >= min3:
		j_object["progress"][2]["percent"] = int(min(100, max(100*float((n-min3)/(max3-min3)),0)))
	##############################################################################
	# Temp
	magnitude = 5
	period = float(m.pi/50)
	offset = 25
	j_object["temperature"] = int(magnitude*m.sin(period*n) + offset)

	return


node_00 = {}
node_00["name"] = "node00"
node_00["cores"] = 0
node_01 = {}
node_01["name"] = "node01"
node_01["cores"] = 0
node_02 = {}
node_02["name"] = "node02"
node_02["cores"] = 0
node_03 = {}
node_03["name"] = "node03"
node_03["cores"] = 0
node_04 = {}
node_04["name"] = "node04"
node_04["cores"] = 0
node_05 = {}
node_05["name"] = "node05"
node_05["cores"] = 0
node_06 = {}
node_06["name"] = "node06"
node_06["cores"] = 0

j_object = {}
j_object["progress"] = []
j_object["temperature"] = 23
j_object["nodes"] = [node_00, node_01, node_02, node_03, node_04, node_05, node_06]

if __name__ == "__main__":
	run()
