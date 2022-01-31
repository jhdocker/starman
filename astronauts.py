import requests

people = requests.get("http://api.open-notify.org/astros.json").json()
iss = requests.get("http://api.open-notify.org/iss-now.json").json()

# for p in request['people']:
# 	print(f"{p['name']} is on the craft: {p['craft']}")

def people_in_space(people):
	print(people['message'])
	if people['message'] =='success':
		return people
	else:
		print(f'there seems to be a problem with the astronauts endpoint')

def get_iss_position(position):
	if(position['message'] == 'success'):
		return position
	else:
		print(f'there seems to be a problem with the position endpoint')

print(people_in_space(people))

print('iss:')
print(get_iss_position(iss))
