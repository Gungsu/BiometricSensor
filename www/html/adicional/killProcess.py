import os
import signal
#ps -ef | grep python
os.system('ps -ef | grep main.py > tmp')
output = open('tmp', 'r').read()

outputLines = output.split("\n")
contador = 0
for a in outputLines:
        if a.count('main.py') > 0:
                proc = a.split(" ")
                for pproc in proc:
                        if pproc.isdigit():
                                proc1 = pproc
                                break
                break
        contador += 1
proc = int(proc1)
os.kill(proc, signal.SIGTERM)
