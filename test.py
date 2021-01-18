import os
import sys
from datetime import datetime
import time

os.environ["TZ"] = 'America/Los_Angeles'
time.tzset()

datetime = datetime.today()

file = open('hello_world.txt', 'a')
file.write(f'Date & Time: {datetime}\n')
file.close()

sys.exit(f"Successfull")