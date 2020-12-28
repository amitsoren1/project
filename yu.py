import subprocess
process = subprocess.Popen(['curl', 'https://get.acme.sh', '|', 'sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process.wait() # Wait for process to complete.

# iterate on the stdout line by line
for line in process.stdout.readlines():
    print(line.decode("utf-8"))

print("ERROR")

for line in process.stderr.readlines():
    print(line)
