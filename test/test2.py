import subprocess

full_output = subprocess.check_output(["sudo","iptables", "-vL", "INPUT"], universal_newlines=True)

# def get_lines(full_messege):
#     lines = full_output.split("\n")
#     return lines
#chain_name = get_lines(full_output)
#print(chain_name[0])

lines = full_output.split("\n")
chain_name = lines[0]
l = len(lines)
info = (' '.join(lines[2].split())).split(" ")
row = []

for i in range(2, len(lines) - 1):
    row.append(' '.join(lines[i].split()).split(" "))
    # row = (' '.join(lines[i].split())).split(" ")
    # print(row)

print(row)
# print(full_output)
# print(chain_name)
# print()
# print(l)
# print(info)
# print(info2)
# print(lines)
# print()





