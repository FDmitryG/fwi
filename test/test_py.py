import subprocess
#from subprocess import PIPE

# cmd = "iptables -h"
#PIPE = subprocess.PIPE
# p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
#         stderr=subprocess.STDOUT, close_fds=True)
# print(p.stdout.read())

# line = cmd_stdout.stdout.read()
# chains = (line.decode("utf-8")).split("\n")

def get_chains():
    PIPE = subprocess.PIPE
    cmd = "sudo iptables -vLXX | grep Chain | cut -d \  -f2"
    cmd_stdout = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)
    line = str(cmd_stdout.stdout.read(), "utf-8")
    chains = line.splitlines()
    return chains

if __name__ == '__main__':
    print(get_chains())