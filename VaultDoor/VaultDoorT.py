import re
with open('VaultDoorTraining.java', 'r') as file:
    file = file.read()

print(re.findall(r'password.equals\("([A-Za-z0-9_\./\\-]*)"\)', file)[0])

