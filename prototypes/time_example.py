import time
import re
import numpy as np

def main():
	print("""
	#d = Days
	#s = Seconds
	#m = Mins
	""")

	user_time = input("[:] ")
	
	if 'd' in user_time:
		print('Message will send in ' + user_time)
		convert_number = "".join(re.findall(r'\d+', user_time)) # Extracts number from user_time
		convert_time = int(convert_number) # Converts the list into a integer
		time.sleep(86400 * convert_time) # 86400 seconds equals one day 
	elif 's' in user_time:
		pass
	elif 'm' in user_time:
		pass
	else:
		print('Wrong input..')


if __name__ == '__main__':
	main()
