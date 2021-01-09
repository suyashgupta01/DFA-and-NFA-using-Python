N = input("Enter number of states N in the DFA (the states will be 0 through N-1): ")
# states = 0,1,2,....N-1

num_of_accepting_states = input("Enter number of accepting states: ")
accepting_states = [] 
for i in range(int(num_of_accepting_states)):
    accepting_states.append(input("Enter accepting state " + str(i) + ': '))

M = input("Enter number of symbols M in the alphabet: ")
alphabet = input("Enter the alphabet: ")

num_of_regular_transitions = input("Enter number of regular transitions: ")
regular_transitions = []
print("Regular transition format: <old_state,input,new_state>")
for i in range(int(num_of_regular_transitions)):
    regular_transitions.append(input("Enter regular transition " + str(i) + ': '))

num_of_epsilon_transitions = input("Enter number of epsilon transitions: ")
epsilon_transitions = []
print("Epsilon transition format: <old_state,new_state>")
for i in range(int(num_of_epsilon_transitions)):
    epsilon_transitions.append(input("Enter epsilon transition " + str(i) + ': '))

nfa_input = input("Enter input for the NFA: ")

regular_transitions_list = [] # A list of lists of the format: old_state,input,new_state
for i in regular_transitions:
    regular_transitions_list.append(i.split(','))
    
epsilon_transitions_list = [] # A list of lists of the format: old_state,new_state
for i in epsilon_transitions:
    epsilon_transitions_list.append(i.split(','))

current_states = {0} # using a set here to not having to deal with duplicates 
for inputt in nfa_input:
    new_current_states = set()
    
    if inputt not in alphabet:
        sys.exit(inputt + ' not in alphabet')
    
    list_of_current_states = list(current_states) # creating list as set is not subscriptable
    
    for i in regular_transitions_list: 
        for j in list_of_current_states:
            if str(i[0]).strip() == str(j).strip() and str(i[1]).strip() == str(inputt).strip():
                print("old_state,input,new_state: ",i)
                new_current_states.add(i[2])
                
    for i in epsilon_transitions_list:
        for j in list_of_current_states:
            if str(i[0]).strip() == str(j).strip():
                new_current_states.add(i[1])
    
    current_states = new_current_states
            
accepted = False
for i in current_states:
    if i in accepting_states:
        print('Accepted')
        accepted = True
        break
        
if not accepted:
    print('Not accepted')

# note: using strip() to remove trailing spaces while comparision