class AutoSender(object):
	def main(self):
		self.email = input('Email: ')
		self.password = input('Password: ')

	def wait_time(self):
		self.time = input('Time: ')

	def send(self):
		self.main()
		self.wait_time()
		print(self.password)
		print(self.time)
		print(self.email)


obj = AutoSender()
obj.send()
