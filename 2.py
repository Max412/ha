import requests, sys, os

adm = []

for n in range(0, 256):
      for i in range(0, 256):
        admin_url = f"http://192.168.{n}.{i}/"
        print(f'192.168.{n}.{i}')
        try:
            response = requests.get(admin_url, timeout=0.01)
            if response.status_code == 200 or response.status_code == 401:
            	print(f"Found admin page at 192.168.{n}.{i}")
            	adm.append(f'192.168.{n}.{i}')
        except requests.exceptions.ReadTimeout:
         try:
            response = requests.get(admin_url, timeout=2)
            print(response.status_code)
            if response.status_code == 200 or response.status_code == 401:
            	print(f"Found admin page at 192.168.{n}.{i}")
            	adm.append(f'192.168.{n}.{i}')
         except:
         	pass
        except:
        	pass


print('\nAdmin page(-s):')
for ok in adm:
	print(ok)

input('\nEND')