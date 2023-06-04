inp = 's0,s1,s2,s3,s4,s5,s6,s7'
inp_list = [int(x[1:]) for x in inp.split(',')]
print(inp_list)

soln = []
variables = ['p','q','a','o']

for i in inp_list:
    temp_soln = []
    val = list(str(bin(i))[2:].zfill(4))
    
    for j in range(4):
        if val[j] == '1':
            temp_soln.append(variables[j])
        else:
            temp_soln.append('!'+variables[j])
    
    soln.append('&'.join(temp_soln))

soln = '|'.join(soln)

print(soln)
