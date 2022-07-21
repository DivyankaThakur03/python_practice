# run a bash script using python

#Python has a built-in module called subprocess which is used to execute the commands and scripts inside Python scripts

import subprocess

#subprocess.run(["ls","-la"])
#print("hi")

#result = subprocess.run(["cat", "list.py"], stderr=subprocess.PIPE, text=True)
#print(result.stderr)

subprocess.call('./bash_python.sh')

