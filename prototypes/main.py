
def main():
	print("1. Google")
	print("2. Protonmail")
	service = input("> ")
	if service == 1 or 'google'.lower():
		googleaccount()
	elif service == 2 or 'protonmail'.lower():
		protonaccount()

def googleaccount():
	pass



def protoaccount():
	pass


if __name__ == '__main__':
	main()
