#!/usr/bin/python
import sys
from os import _exit as salir


def op_nop(stack, line_number, number, opcode):
    return


def op_add(stack, line_number, number, opcode):
    if (len(stack) < 2):
        manage_error(line_number, 8, None)

    sum = stack[-1] + stack[-2]
    stack[-2] = sum
    stack.pop()


def op_pop(stack, line_number, number, opcode):
    if (len(stack) == 0):
        manage_error(line_number, 6, None)
    else:
        stack.put_off()


def op_pall(stack, line_number, number, opcode):
    stack.print_all();


def op_push(stack, line_number, number, opcode):
    if not number:
        manage_error(line_number, 4, None)
    if (isinstance(int(line_number), int) is False):
        manage_error(line_number, 4, None)
    else:
        stack.push(number)


def op_pint(stack, line_number, number, opcode):
    if (len(stack) == 0):
        manage_error(line_number, 5, None)
    else:
        print(stack[-1])


def op_swap(stack, line_number, number, opcode):
    if (len(stack) < 2):
        manage_error(line_number, 7, None)
    else:
        stack[-1], stack[-2] = stack[-2], stack[-1]


def error_none_op(stack, line_number, number, opcode):
    manage_error(line_number, 2, opcode)


# Print error to the stderr and exit with a failure status
def manage_error(line_number, error, name):
    if error == 0:
        sys.stderr.write("USAGE: monty file\n")
    elif error == 1:
        sys.stderr.write("Error: Can't open file {}\n".format(name))
    elif error == 2:
        sys.stderr.write("L{}: unknown instruction {}\n".format(line_number, name))
    elif error == 4:
        sys.stderr.write("L{}: usage: push integer\n".format(line_number))
    elif error == 5:
        sys.stderr.write("L{}: can't pint an empty stack\n".format(line_number))
    elif error == 6:
        sys.stderr.write("L{}: can't pop, stack empty\n".format(line_number))
    elif error == 7:
        sys.stderr.write("L{}: can't swap, stack too short\n".format(line_number))
    elif error == 8:
        sys.stderr.write("L{}: can't add, stack too short\n".format(line_number))
    exit(1)
