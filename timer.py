import time
import checker

updated = False
log = []

while True:
    if not updated:
        start = time.time()
        updated = True
    finish = time.time()
    if finish - start == 60:
        updated = False
        execfile("checker.py")
        
        
