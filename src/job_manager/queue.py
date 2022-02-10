# Struct to hold Jobs for the Manager
from job_manager.job import Job

class Queue():
	def __init__(self):
			self.jobs = []

	def add_job(self, job):
		self.jobs.append(job)

	def rm_job(self, job_id):
		for job in self.jobs:
			if job.get_id() == job_id:
				self.jobs.remove(job)
				break

	def get_jobs(self):
		return self.jobs
