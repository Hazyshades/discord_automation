import datetime

import time
from datetime import datetime

def timet():
    #1
    mytime = time.ctime()
    now1 = "11:38"
    print(now1)

    #2
    now2 = datetime.now().strftime("%I:%M")
    if now1 < now2:
        print(now2)

if __name__ == '__main__':
    timet()
