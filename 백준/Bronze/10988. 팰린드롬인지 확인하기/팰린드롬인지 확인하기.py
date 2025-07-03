s = input()
chars = list(s)
length = len(chars)

if chars[0:length] == chars[0:length][::-1]:
  print('1')

else:
  print('0')
