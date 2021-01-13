import os
import sys
from datetime import datetime
import time

os.environ["TZ"] = 'America/Los_Angeles'
time.tzset()

print('Date & Time:', datetime.today())
sys.exit(f"Successfull")