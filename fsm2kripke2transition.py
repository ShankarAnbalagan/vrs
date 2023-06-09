transition_relation = '!a&next(p)&next(q)'
fsm_variables = ['p','q','a', 'next(p)', 'next(q)']
kripke_variables = ['p','q','a', 'next(p)', 'next(q)', 'next(a)']
remove_states = 's1,s3,s5,s7'

transition_relation_vars = transition_relation.split('&')

kripke_transition_relation_vars = transition_relation_vars
kripke_transition_relation_vars.append('!next(a)')

fsm_variables_len = len(fsm_variables)
kripke_variables_len = len(kripke_variables)

fsm_transition_relation = []
kripke_transition_relation = []
kripke_transition_relation_removed = []

for i in range(2**fsm_variables_len):
    temp_soln = []
    b = list(str(bin(i))[2:].zfill(fsm_variables_len))

    for index, j in enumerate(b):
        if j == '1':
            temp_soln.append(fsm_variables[index])
        else:
            temp_soln.append('!'+fsm_variables[index])

    if set(transition_relation_vars).issubset(set(temp_soln)):
        fsm_transition_relation.append(temp_soln)


for i in range(2**kripke_variables_len):
    temp_soln = []
    b = list(str(bin(i))[2:].zfill(kripke_variables_len))

    for index, j in enumerate(b):
        if j == '1':
            temp_soln.append(kripke_variables[index])
        else:
            temp_soln.append('!'+kripke_variables[index])

    if set(kripke_transition_relation_vars).issubset(set(temp_soln)):
        kripke_transition_relation.append(temp_soln)


#full_transition_relation = '|'.join(full_transition_relation)

print('FSM Transitions')
for r in fsm_transition_relation:
    print(r)
print()
print('Kripke Transitions')
for r in kripke_transition_relation:
    print(r)
print()
if remove_states != '':
    remove_states_list = [int(x[1:]) for x in remove_states.split(',')]

    soln = []
    variables = ['p','q','a']

    for i in remove_states_list:
        temp_soln = []
        val = list(str(bin(i))[2:].zfill(len(variables)))
        
        for j in range(len(variables)):
            if val[j] == '1':
                temp_soln.append(variables[j])
            else:
                temp_soln.append('!'+variables[j])
        
        soln.append(temp_soln)

    print('States to be removed')
    print(soln)
    print()

    for r1 in soln:
        for r2 in kripke_transition_relation:
            if r2 not in kripke_transition_relation_removed and not set(r1).issubset(set(r2)):
                kripke_transition_relation_removed.append(r2)
    
    print('Kripke Transitions with removed states')
    for r in kripke_transition_relation_removed:
        print(r)

    print()
    soln = []
    print('In DNF')
    for r in kripke_transition_relation_removed:
    
        soln.append('&'.join(r))
    
    soln = '|'.join(soln)

    print(soln)