"""import"""
import secrets
import os
import random
import time

# i refuse to use uuid.uuid7() lol

OUTPUT = ''

def insert(og: str,
           ins: str,
           idx: int) -> str:
    """
    Insert a string into a string
    at a certain index.
    """
    return og[:idx] + ins + og[idx:]

print("Version: 7")

UUID = ''
ADD = ''

EPOCH = round(time.time() * 1000)
EPOCHMILLI = format(EPOCH, 'x')

UUID = '0' + EPOCHMILLI + '-'


UUID = insert(UUID, '-', 8) + '7'

ADD = secrets.token_hex(2)[:3]
UUID = UUID + ADD + '-'

UUID = UUID + hex(random.randint(8, 11))

ADD = secrets.token_hex(2)[:3]
UUID = UUID + ADD + '-'

ADD = secrets.token_hex(6)
UUID = UUID + ADD

os.system(f"echo 'uuid={UUID}' >> $GITHUB_OUTPUT")
os.system("echo 'safe=safe' >> $GITHUB_OUTPUT")
