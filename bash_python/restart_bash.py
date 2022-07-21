from datetime import datetime
import os 
import psutil
import subprocess

start1 = datetime.now()
subprocess.call('bash_python/bash_python.sh')
end1 = datetime.now()

print("Time requires for subprocess is -",end1 - start1)

start2 = datetime.now()
os.system("sh bash_python/bash_python.sh")
end2 = datetime.now()

print("Time required for os is -", end2-start2)

t1 = (end1 -start1/end2-start2)*100
print(t1)