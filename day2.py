import numpy as np

def cpu(opcode):
    i = 0
    while True:
        code = opcode[i]
        if code == 1 or code == 2:
            eli1, eli2, eli3 = opcode[i + 1: i + 4]
            el1, el2 = opcode[eli1], opcode[eli2]
            if code == 1:
                opcode[eli3] = el1 + el2
            else:
                opcode[eli3] = el1 * el2
            i += 4
        elif code == 99:
            return opcode
        else:
            raise KeyError("wrong opcode encountered!")


def run_program(opcode, noun, verb):
    opcode_new = list(opcode)
    opcode_new[1] = noun
    opcode_new[2] = verb
    return cpu(opcode_new)[0]


def brute_force_program(opcode, result):
    for i in range(100):
        for j in range(100):
            if run_program(opcode, i, j) == result:
                return 100 * i + j
    return -1


def efficient_brute_force(opcode, result):
    init = run_program(opcode, 0, 0)
    start = result - init
    i = start//300000
    for j in range(100):
        if run_program(opcode, i, j) == result:
            return 100 * i + j
    return -1


if __name__ == "__main__":
    opcode = [int(x) for x in open("day2.1.txt", "r").readlines()[0].split(",") if len(x.strip())]
    print(run_program(opcode, 12, 2))
    print(efficient_brute_force(opcode, 19690720))
