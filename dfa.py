N = input("Enter number of states N in the DFA (the states will be 0 through N-1): ")
# states = 0,1,2,....N-1

num_of_accepting_states = input("Enter number of accepting states: ")
accepting_states = [] 
for i in range(int(num_of_accepting_states)):
    accepting_states.append(input("Enter accepting state " + str(i) + ': '))

M = input("Enter number of symbols M in the alphabet: ")
alphabet = input("Enter the alphabet: ")

num_of_transitions = input("Enter number of transitions: ")
transitions = []
print("Transition format: <old_state,input,new_state>")
for i in range(int(num_of_transitions)):
    transitions.append(input("Enter transition " + str(i) + ': '))

dfa_input = input("Enter input for the DFA: ")

transitions_list = [] # A list of lists of the format: old_state,input,new_state
for i in transitions:
    transitions_list.append(i.split(','))

current_state = 0
for inputt in dfa_input:
    if inputt not in alphabet:
        sys.exit(inputt + ' not in alphabet')
    for i in transitions_list:
#         print(i[0], current_state, '  ' ,i[1], inputt)
        if str(i[0]).strip() == str(current_state).strip() and str(i[1]).strip() == str(inputt).strip():
            print("old_state,input,new_state: ",i)
            current_state = i[2]
            
if str(current_state) in accepting_states:
    print('Accepted')
else:
    print('Not accepted')


# note: using strip() to remove trailing spaces while comparision