import sys


class TuringMachine(object):
    def __init__(self):
        self.input_alphabet = []
        self.tape_alphabet = []
        self.whitespace = []
        self.states = []
        self.initial_state = []
        self.final_states = []
        self.number_of_tapes = []
        self.transitions = []


tm = []
fp = []

for i in range(2):
    tm.append(TuringMachine())
    fp.append(open(sys.argv[i+1], "r"))
    lines_cmd = fp[i].readlines()
    fp[i].close()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    lines = lines[1:]
    tm[i].input_alphabet = lines[0].split()
    tm[i].tape_alphabet = lines[1].split()
    tm[i].whitespace = lines[2]
    tm[i].states = lines[3].split()
    tm[i].states = [int(p) for p in tm[i].states]
    tm[i].states.sort()
    tm[i].initial_state = lines[4]
    tm[i].final_states = lines[5].split()
    tm[i].number_of_tapes = lines[6]
    for j in range(7, len(lines)):
        tm[i].transitions.append(lines[j].split())


def printTmData(tm_aux, i):
    print()
    print(f'Alfabeto da máquina {i+1} : {tm_aux.input_alphabet}')
    print(f'Alfabeto da fita da máquina {i+1} : {tm_aux.tape_alphabet}')
    print(f'Branco da máquina {i+1} : {tm_aux.whitespace}')
    print(f'Estados da máquina {i+1} : {tm_aux.states}')
    print(f'Estado incial da máquina {i+1} : {tm_aux.initial_state}')
    print(f'Estado final da máquina {i+1} : {tm_aux.final_states}')
    print(f'N de fitas da máquina {i+1} : {tm_aux.number_of_tapes}')
    print(f'Transições da máquina {i+1}')
    for j in tm_aux.transitions:
        print(j)
    print()


# if tm[0].number_of_tapes != tm[1].number_of_tapes:
tm.append(TuringMachine())

# Função 2a linha
for j in range(len(tm[0].input_alphabet)):
    tm[2].input_alphabet.append(tm[0].input_alphabet[j])


for i in range(len(tm[1].input_alphabet)):
    if tm[1].input_alphabet[i] not in tm[0].input_alphabet:
        tm[2].input_alphabet.append(tm[1].input_alphabet[i])
#######################################################

# Função 3a linha
for j in range(len(tm[0].tape_alphabet)):
    tm[2].tape_alphabet.append(tm[0].tape_alphabet[j])


for i in range(len(tm[1].tape_alphabet)):
    if tm[1].tape_alphabet[i] not in tm[0].tape_alphabet:
        tm[2].tape_alphabet.append(tm[1].tape_alphabet[i])

#######################################################

# Função linha4
letter = 65
for i in range(26):
    if chr(letter) not in tm[2].tape_alphabet:
        tm[2].whitespace.append(chr(letter))
        break
    letter += 1

#######################################################

# Define estados
tam_final = len(tm[0].states) + len(tm[1].states) + 1

for i in range(tam_final):
    tm[2].states.append(i)

# linha 5

# matriz_ref_states = [[], []]

# states = 1
# for i in range(2):
#     var = len(tm[i].states)
#     for j in range(var):
#         matriz_ref_states[i].append(states)
#         states += 1


# matriz_ref_init = [[], []]

# tm[2].initial_state.append(0)
# for i in range(2):
#     matriz_ref_init[i].append(tm[i].initial_state[0])


# matriz_ref_final = [[], []]

# for i in range(2):
#     var2 = len(tm[i].final_states)
#     for j in range(var2):
#         matriz_ref_final[i].append(tm[i].final_states[j])

# # for j in range(2):
# #     for i in range(len(matriz_ref_final[0] + len(matriz_ref_final[1]))):
# #         tm[2].final_states.append(matriz_ref_states[j][i])

tm[2].initial_state.append('0')

ref_tm1 = []


for i in range(3):
    printTmData(tm[i], i)

# print(matriz_ref_states)
# print(matriz_ref_init)
# print(matriz_ref_final)
