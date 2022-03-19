import json

events = open('opportunity_data.txt', 'r')
events_dict = json.loads(events.read())
events.close()

def authenticate(email, password):
  with open('users.json') as users:
    listObj = json.load(users)
  for user in listObj:
    if user["email"] == email:
      return user["password"] == password
  return False

def create_user(email, password, dob):
  with open('users.json') as users:
    listObj = json.load(users)
  listObj.append({
    "email": email,
    "password": password,
    "hours": 0,
    "DOB": dob
  })
  with open('users.json', 'w') as users:
    json.dump(listObj, users, indent=2, separators=(',',': '))

def get_user(email):
  with open('users.json') as users:
    listObj = json.load(users)
  for user in listObj:
    if user["email"] == email:
      return user
  return None

def register(user, eventID):
  update_service_hours(user, events_dict[evenrID]["length"])

def get_service_hours(email):
  with open('users.json') as users:
    listObj = json.load(users)
  for user in listObj:
    if user["email"] == email:
      return user["hours"]

def update_service_hours(user, hours):
  with open('users.json') as users:
    listObj = json.load(users)
  for i in range(len(listObj)):
    if listObj[i]["email"] == user:
      listObj[i]["hours"] += hours
  with open('users.json', 'w') as users:
    json.dump(listObj, users, indent=2, separators=(',',': '))
