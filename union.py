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
    tm[i].initial_state = [int(p) for p in tm[i].initial_state]
    tm[i].final_states = lines[5].split()
    tm[i].final_states = [int(p) for p in tm[i].final_states]
    tm[i].number_of_tapes = lines[6]
    tm[i].number_of_tapes = [int(p) for p in tm[i].number_of_tapes]
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


# estado inicial
tm[2].initial_state.append('0')

ref_states = [[], []]


# referencia de estados
for i in range(len(tm[0].states)):
    ref_states[0].append(i+1)

for i in range(len(tm[1].states)):
    ref_states[1].append(len(tm[0].states) + 1 + i)

# define estado final
for i in range(2):
    for j in range(len(tm[i].final_states)):
        tm[2].final_states.append(
            ref_states[i][tm[i].final_states[j]])

# define n de fitas

tm[2].number_of_tapes.append(tm[0].number_of_tapes[0])

######################################

for i in range(3):
    printTmData(tm[i], i)
