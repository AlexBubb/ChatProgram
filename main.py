import init
import rsafun
import screenfun
import wordstonum
import account
import message
people = []
pubkeys = {}
logincodes = {}

a = init.start()
people = a[0]
logincodes = a[1]

while True:
  username = init.login(logincodes)
  if username == None:
    print("Failed to authenticate!")
  else:
    privkey = username[1]
    username = username[0]
    break
while True:
  choice = "aaa"
  #refresh the people and pubkeys varibles in case of changes
  a = init.refresh(pubkeys)
  people = a[0]
  pubkeys = a[1]
  screenfun.clear()
  print("Welcome")
  print("Please choose one of the following options:")
  print("1. Generate RSA key pair")
  print("2. list avalible people")
  print("3. Add a new accout")
  print("4. Send a message")
  print("5. Read incoming a messages")
  print("6. Exit")
  choice = input("Enter your choice: ")

  if choice == "1":
    screenfun.clear()
    rsafun.createKeyPair()

  if choice == "2":
    screenfun.clear()
    account.listPeople()

  if choice == "3":
    screenfun.clear()
    account.create()
    
  if choice == "4":
    screenfun.clear()
    message.send(pubkeys,username)

  if choice == "5":
    screenfun.clear()
    message.read(username,privkey)

  if choice == "6":
    screenfun.clear()
    quit()
  if choice == "clear":
    with open("keys.txt", "w") as f:
      f.write("")
    with open("people.txt", "w") as f:
      f.write("")
    with open("logincodes.txt", "w") as f:
      f.write("")
