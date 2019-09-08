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
    tm[i].initial_state = lines[4]
    tm[i].final_states = lines[5].split()
    tm[i].number_of_tapes = lines[6]
    for j in range(7, len(lines)):
        tm[i].transitions.append(lines[j])


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


for i in range(2):
    printTmData(tm[i], i)
