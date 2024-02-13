import wordstonum
import rsafun


def listPeople():
  with open("people.txt", "r") as f:
    people = f.readlines()
  for person in people:
    print(person)
  input("Press enter to continue...")


def create():
  #saves name and public key to correct places
  name = input("Enter the name of the person you want to add: ")
  with open("people.txt", "a") as f:
    f.write(name + "\n")
  pubkey = input("Enter the public key of the person you want to add: ")
  with open("keys.txt", "a") as f:
    f.write(pubkey + "\n")
  #makes pubkey a list
  pubkey = pubkey.strip('][').split(', ')
  for x in range(len(pubkey)):
    pubkey[x] = int(pubkey[x])
  #uses public key to encrypt a code for account verification
  with open("logincodes.txt", "a") as f:
    f.write(str(rsafun.encrypt(wordstonum.stringToNum("succes"), pubkey[0],pubkey[1]))+"\n")
  #sets up the beggining of messages
  with open(name + ".txt", "w") as f:
    num = wordstonum.stringToNum("Start of messages.")
    f.write(str(rsafun.encrypt(num, pubkey[0], pubkey[1])))
