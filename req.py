def scan(url, ch):
	import requests 
	if "1" in ch:
		print("#" * 50, "Loading...\n")
		print("Trying GET method to connect to", url,"\n")
		response = requests.get(url)
		if response:
			print("#" * 50, "Success!")
		else:
			print("#" * 50, "Failled!")
		print("Status code sent by server at", url, "\n")
		print(response.status_code)
		print("Headers sent by server at", url, "\n")
		print(response.headers)
		print("#" * 50, "Finished!")
		print("#" * 25, "Switching again!", "#" * 25, "\n")
		print("Finished communicating with server at", url, "\n")
		start()
	elif "2" in ch:
		print("#" * 50, "Loading...\n")
		print("Trying POST method to connect to", url,"\n")
		response = requests.post(url)
		if response:
			print("#" * 50, "Success!")
		else:
			print("#" * 50, "Failled!")
		print("Status code sent by server at", url, "\n")
		print(response.status_code)
		print("Headers sent by server at", url, "\n")
		print(response.headers)
		print("#" * 50, "Finished")
		print("#" * 25, "Switching again!", "#" * 25, "\n")
		print("Finished communicating with server at", url, "\n")
		start()
	else:
		print("#" * 25, "Error getting choice!\n")
		print("Please try again...\n")
		start()
def start():
	print("#" * 50, "Loading...\n")
	print("Please enter url\n")
	print("Allowed formart: http(s)://example.domain/path\n")
	url = input("=> ")
	print("#" * 50, "Accessing...\n")
	print("#" * 25, "Using ", url, "as host\n")
	print("#" * 50, "\n")
	print("Use GET or POST?\n")
	print("1 = GET")
	print("2 = POST")
	scan(url, input("=> "))
start()

