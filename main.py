from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import time, os, re, sys, getpass
import smtplib, ssl, email

class AutoSender(object):
	def main(self):
		print("""
    _         _       ____                 _
   / \  _   _| |_ ___/ ___|  ___ _ __   __| | ___ _ __
  / _ \| | | | __/ _ \___ \ / _ \ '_ \ / _` |/ _ \ '__|
 / ___ \ |_| | || (_) |__) |  __/ | | | (_| |  __/ |
/_/   \_\__,_|\__\___/____/ \___|_| |_|\__,_|\___|_|
	Author @ github: kenjidoom
""")	# ASKING USER INPUT DATA
		self.email = input('[+] Email: ')
		self.password = getpass.getpass('[+] Password: ')
		self.recv = input('[+] Reciver: ')
		self.subject = input('[+] Subject: ')
		self.body = input('[+] Message: ')
		self.attachment = input('[+] Attachment: ')

		# FORMATTING EMAIL HERE
		self.message = MIMEMultipart()
		#self.message.set_content(self.body)
		self.message['Subject'] = self.subject
		self.message['From'] = self.email
		self.message['To'] = self.recv
		self.message.attach(MIMEText(self.body, "plain"))

		if os.path.exists(self.attachment):
			with open(self.attachment, 'rb') as file:
				self.part = MIMEBase("application", "zip")
				self.part.set_payload(file.read())
		else:
			print('[-] No File Found')

		# CHECKING IF CREDS ARE VALID
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
		self.time = input('[+] Time: ')
		if 'd' in self.time.lower():
			print('[+] Waiting ' + self.time)# Self-Note: r'\d+' = rejex for numbers
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
		encoders.encode_base64(self.part)
		self.part.add_header(
		"Content-Disposition",
		f"attachment; filename={self.attachment}")
		self.message.attach(self.part) # For some reason this does not work
		self.text = self.message.as_string()
		print('[+] Sending message....')
		# This will run after the time is done.
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
			server.login(self.email, self.password)
			server.sendmail(self.email, self.recv, self.text)
			print('[+] Sent.')


obj = AutoSender()
obj.send()
