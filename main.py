import smtplib, ssl
import time, os

class AutoSender(object):
	def main(self):
		self.email = input('Email: ')
		self.password = input('Password: ')
		self.recv = input('Reciver: ')
		self.subject = input('Subject: ')
		self.message = input('Message: ')
		self.attachment = input('Attachment: ')
		os.system('clear')

	def wait_time(self): # Time Function
		print("""
		d = days
		m = minutes
		s = seconds
		""")
		self.time = input('Time: ')
		if 'd' in self.time:
			convert_number = "".join(re.findall(r'\d+', self.time))
			convert_time = int(convert_number)
			time.sleep(86400 * convert_time)
		elif 'm' in self.time:
			convert_number = "".join(re.findall(r'\d+', self.time))
			convert_time = int(convert_number)
			time.sleep(60 * convert_time)
		elif 's' in self.time:
			convert_number = "".join(re.findall(r'\d+', self.time))
			convert_time = int(convert_number)
			time.sleep(1 * convert_time)


	def send(self): # Sending email in the end
		self.main()
		self.wait_time()


obj = AutoSender()
obj.send()
