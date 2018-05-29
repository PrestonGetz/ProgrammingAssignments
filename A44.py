from datetime import*
import time
import replit

while True:
    now=datetime.now()-timedelta(hours=6)
    print(str(15-now.day)+" days\n")
    print(str(14-now.hour)+" hours\n")
    print(str(49-now.minute)+" minutes\n")
    print(str(59-now.second)+" seconds")
    
    time.sleep(1)
    replit.clear()
