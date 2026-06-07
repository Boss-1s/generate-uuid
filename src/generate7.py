"""import"""
import os
import time

# i refuse to use uuid.uuid7() lol

OUTPUT = ''

def insert(str1, str2, index):
    "insert text at index"
    original = str1
    new = str2
    pos = index

    global OUTPUT
    OUTPUT = original[:pos] + new + original[pos:]

print("Version: 7")

UUID = ''
ADD = ''

EPOCH = round(time.time() * 1000)
EPOCHMILLI = format(EPOCH, 'x')

UUID = '0' + EPOCHMILLI + '-'

insert(UUID, '-', 8)
UUID = OUTPUT + '7'

ADD = os.urandom(2).hex()[:-1]
UUID = UUID + ADD + '-'

ADD = os.urandom(2).hex()
UUID = UUID + ADD + '-'

ADD = os.urandom(6).hex()
UUID = UUID + ADD

os.system(f"echo 'uuid={UUID}' >> $GITHUB_OUTPUT")
os.system("echo 'safe=safe' >> $GITHUB_OUTPUT")
