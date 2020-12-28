import subprocess,os
os.chdir(os.path.join(os.getcwd(),"acme.sh"))
# process = subprocess.Popen(['git', 'clone', 'https://github.com/acmesh-official/acme.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process = subprocess.Popen(['./acme.sh','--install'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

process.wait() # Wait for process to complete.

# iterate on the stdout line by line
for line in process.stdout.readlines():
    print(line.decode("utf-8"))

print("ERROR")

for line in process.stderr.readlines():
    print(line)
