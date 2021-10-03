import requests
#import threading
domain = input("Enter domain: ")
file = open('dic.txt','r')
content = file.read()

dicts = content.splitlines()

for dict in dicts:
	url1 = f"http://{domain}/{dict}"
	url2 = f"https://{domain}/{dict}"
	try:
		requests.get(url1)
		print(f"Discovered URL: {url1}")
		requests.get(url2)
		print(f"Discovered URL: {url2}")
	except requests.ConnectionError:
		pass
