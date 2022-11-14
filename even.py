import re

# word = input('Enter a word')
# pattern = r'ne'
# if re.match(pattern, word):
#     print('Match')
# else:
#     print('No match')
#

# email = 'nelsong@mail.com'
# pattern = r'@'
# if re.search(pattern, email):
#     print('Match')
# else:
#     print('No match')

# pattern = r'c..n'
# if re.match(pattern, 'coin'):
#     print('match')

# emails = '''
#         nelson@gmail.com
#         jae-net@edu.net.
#         Text.good_1234@gov.ng
# '''
# pattern = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-z]+')
# matches = pattern.finditer(emails)
# for match in matches:
#     print(match)
from threading import *
from time import sleep

class Nelson(Thread):
    def run(self):
        for i in range(10):
            print('nelson')
            sleep(1)

class Wisdom(Thread):
    def run(self):
        for i in range(10):
            print('wisdom')
            sleep(1)


n = Nelson()
w = Wisdom()
n.start()
sleep(0.2)
w.start()
