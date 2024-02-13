"""
def stringToNum(string):
  number = ''
  for char in string:
    num = str(ord(char))
    if len(num) == 1:
      num = '00' + num
    elif len(num) == 2:
      num = '0' + num
    number += num
  return int(number)


def numToString(num):
  string = ''
  num = str(num)
  for i in range(len(num)):
    if i % 3 == 0:
      string += chr(int(num[i:i + 3]))
  return string
"""


def numToString(num):
  st = ""
  while (num != 0):
    temp = num % 256
    st += chr(temp)
    chr(temp)
    num = num - temp
    num = num // 256
  st = st[::-1]
  return st


def stringToNum(message):
  grd = 1
  num = 0
  message = message[::-1]
  for i in range(0, len(message), +1):
    num = num + ord(message[i]) * grd
    grd *= 256
  return num
