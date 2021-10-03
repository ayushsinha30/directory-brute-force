import requests
#import threading
domain = input("Enter domain: ")
file = open('dic.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
	url1 = f"http://{domain}/{subdomain}"
	url2 = f"https://{domain}/{subdomain}"
	try:
		requests.get(url1)
		print(f"Discovered URL: {url1}")
		requests.get(url2)
		print(f"Discovered URL: {url2}")
	except requests.ConnectionError:
		pass
