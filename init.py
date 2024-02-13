import wordstonum
import rsafun

#sets up starting varibles
def start():
  logincodes = {}
  with open("people.txt", "r") as f:
    people = f.readlines()
  for person in people:
    person = person.strip()
  with open("logincodes.txt", "r") as f:
    for person in people:
      person = person.strip('\n')
      logincodes[person] = f.readline().strip('\n')
      logincodes[person] = int(logincodes[person])
  return [people,logincodes]
#account verifacation
#if the users keys correspond to a login code encrypted with them, then the user is authenticated
def login(logincodes):
  username = input("Username: ")
  if username == "guest":
    return [username, [1,1]]
  privkey = input("Enter your private key: ").strip('][\n').split(', ')
  if wordstonum.numToString(rsafun.decrpyt(logincodes[username], int(privkey[0]), int(privkey[1]))) == "succes":
    print("Succesfully logged in.")
    return [username, privkey]
  return None
#refresh the people and pubkeys varibles in case of changes
def refresh(pubkeys):
  #list of people
  with open("people.txt", "r") as f:
    people = f.readlines()
  for person in people:
    person = person.strip()
  #sets the corresponding name to key in pubkeys
  with open("keys.txt", "r") as f:
    for person in people:
      person = person.strip('\n')
      pubkeys[person] = f.readline().strip('][\n').split(', ')
      pubkeys[person] = [int(i) for i in pubkeys[person]]
  return [people, pubkeys]