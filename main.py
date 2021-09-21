import smtplib, ssl
import time, os, re, sys

class AutoSender(object):
	def main(self):
		print("""
    _         _       ____                 _           
   / \  _   _| |_ ___/ ___|  ___ _ __   __| | ___ _ __ 
  / _ \| | | | __/ _ \___ \ / _ \ '_ \ / _` |/ _ \ '__|
 / ___ \ |_| | || (_) |__) |  __/ | | | (_| |  __/ |   
/_/   \_\__,_|\__\___/____/ \___|_| |_|\__,_|\___|_|   
	Author @ github: kenjidoom
""")
		self.email = input('Email: ')
		self.password = input('Password: ')
		self.recv = input('Reciver: ')
		self.subject = input('Subject: ')
		self.message = input('Message: ')
		self.attachment = input('Attachment: ')
		
		gmail_server = smtplib.SMTP('smtp.gmail.com:587')
		gmail_server.starttls()
		try:
			gmail_server.login(self.email, self.password)
			resp = True
			print('[+] Password Correct!')
			gmail_server.quit()
		except:
			resp = False
			gmail_server.quit()
			print('[-] Inccorect Password!')
			sys.exit()
			return resp

		os.system('clear')

	def wait_time(self): # Time Function
		print("""
		d = days
		m = minutes
		s = seconds
		""")
		self.time = input('Time: ')
		if 'd' in self.time.lower():
			print('[+] Waiting ' + self.time)
			convert_number = "".join(re.findall(r'\d+', self.time))
			convert_time = int(convert_number)
			time.sleep(86400 * convert_time)
		elif 'm' in self.time.lower():
			print('[+] Waiting ' + self.time)
			convert_number = "".join(re.findall(r'\d+', self.time))
			convert_time = int(convert_number)
			time.sleep(60 * convert_time)
		elif 's' in self.time.lower():
			print('[+] Waiting ' + self.time)
			convert_number = "".join(re.findall(r'\d+', self.time))
			convert_time = int(convert_number)
			time.sleep(1 * convert_time)
		else:
			print('[-] Wrong time input!')
			sys.exit()

	def send(self): # Sending email in the end
		self.main()
		self.wait_time()
		os.system('clear')
		port = 465
		print('[+] Sending message....')
		# This will run after the time is done.
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
			server.login(self.email, self.password)
			server.sendmail(self.email, self.recv, self.subject)
			print('[+] sent.')




obj = AutoSender()
obj.send()
