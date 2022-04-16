#!/usr/bin/python
import os
import re


code = [ 0,0,0,0,0,0,0,0 ]
temp_results = {}
possible_result = [] 
for i in range(8):
    for j in range(10):
        code[i]= j
        stdinput = "".join(map(str, code))
        cmd = f"echo {stdinput} | time 2>&1 ./pin_checker"
        result= os.popen(cmd).read()
        time = float(re.findall(r'\n([\.\d]+)user', result)[0])
        temp_results[j] = time
    possible_result.append(max(temp_results, key=temp_results.get))
    for i in range(len(possible_result)):
        code[i] = possible_result[i]
print(''.join(map(str, possible_result)))
