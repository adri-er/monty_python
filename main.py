#!/usr/bin/python3
import sys
from functions import *
from stack import Stack


def main():
    stack = Stack()
    line_number = 0
    number = None

    operations = {
        "pall": op_pall,
        "push": op_push,
        "nop": op_nop,
        "pint": op_pint,
        "swap": op_swap,
        "add": op_add,
        "pop": op_pop
    }

    while True:
        print("$ ", end="")
        line = input()
        line_number += 1
        words = line.split()
        if (len(words) == 0):
            continue
        instruction = words[0]
        if len(words) > 1:
            number = words[1]
        else:
            number = None
        operation = operations.get(instruction, error_none_op)
        operation(stack, line_number, number, instruction)

if __name__ == "__main__":
    main()
