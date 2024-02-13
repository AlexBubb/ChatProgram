import rsafun
import wordstonum
import screenfun
def send(pubkeys,username):
  user = input("Enter the name of the person you want to send a message to: ")
  with open(user + ".txt", "a") as f:
    message = input("Enter your message: ")
    #concatinate message
    num = wordstonum.stringToNum(username + ": " + message)
    #encrypt and send message
    f.write("\n")
    f.write(str(rsafun.encrypt(num, pubkeys[user][0], pubkeys[user][1])))
def read(name,privkey):
  with open(name + ".txt", "r") as f:
    messages = f.readlines()
    for line in messages:
      line = line.strip('\n')
      num = rsafun.decrpyt(int(line), int(privkey[0]), int(privkey[1]))
      print(wordstonum.numToString(num))
  input("Press enter to continue...")