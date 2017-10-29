import os

from utils.Modular import Modular
from utils.ModularArithmetics import ModularArithmetics


def display_title_bar():
    os.system('cls')
    print("\n\t***  Modular Arithmetics ***")
    print("\n")
    print("\t[1] Add modular numbers.")
    print("\t[2] Multiply modular numbers.")
    print("\t[3] Modular inverse.")
    print("\t[4] Primitives.")
    print("\t[5] Chinese remainder theorem.")
    print("\t[q] Quit.")


def press_any_key():
    input("\n\tPress any key to continue...")


def add_numbers():
    p = int(input("\n\tSpecify the base: "))
    a = int(input("\tEnter number 1: "))
    b = int(input("\tEnter number 2: "))
    result = Modular(a, p) + Modular(b, p)
    print("\n\tResult: ({0} + {1}) mod {2} = {3}".format(a, b, p, result.value))
    press_any_key()


def multiply_numbers():
    p = int(input("\n\tSpecify the base: "))
    a = int(input("\tEnter number 1: "))
    b = int(input("\tEnter number 2: "))
    result = Modular(a, p) * Modular(b, p)
    print("\n\tResult: ({0} x {1}) mod {2} = {3}".format(a, b, p, result.value))
    press_any_key()


def modular_inverse():
    p = int(input("\n\tSpecify the base: "))
    a = int(input("\tEnter number 1: "))
    result = Modular(a, p).modular_inverse()
    print("\n\tResult: ({0} ^ -1) mod {1} = {2}".format(a, p, result.value))
    press_any_key()


def primitives():
    p = int(input("\n\tSpecify the base: "))
    result = ModularArithmetics.primitives(p)
    print("\n\tResult:")
    print("\t", result)
    press_any_key()


def chinese_remainder_theorem():
    y = [int(x) for x in input("\n\tSpecify the sequence of integers:").split()]
    n = [int(x) for x in input("\n\tSpecify positive integers that are pairwise co-prime:").split()]
    result = ModularArithmetics.chinese_remainder_theorem(y, n)
    print("\n\tResult:")
    print("\t", result)
    press_any_key()


def quit_message():
    display_title_bar()
    print("\n\tTill next time! Bye!")
    press_any_key()

programs = {
    '1': add_numbers,
    '2': multiply_numbers,
    '3': modular_inverse,
    '4': primitives,
    '5': chinese_remainder_theorem,
    'q': quit_message
}

program_id = ''
display_title_bar()
while program_id != 'q':
    display_title_bar()
    program_id = input("\tWhat would you like to do? ")
    if program_id in programs:
        programs[program_id]()
    else:
        print("\tProgram not implemented")
        press_any_key()


