"""
author: Sunil K B

description:
Consider a polynomial of  single variable. Implement the following functions using Doubly linked lists:
Create_Polynomial_List(P)
Display_Polynomial(P)
ADD_Polynomials(P1,P2)
Multiply(P1,P2)

usage:
python3 DSA_1.py
"""

from __future__ import print_function
import re

import sys

if sys.version_info < (3, 0, 0):
    print(__file__ + ' requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating. Run - python3 '+__file__))
    sys.exit(1)


class Node:
    def __init__(self):
        self.coeff = None
        self.power = None
        self.next = None
        self.prev = None


# Create 2 polynomial equations
def create_polynomial_list():
    global equation2
    global equation1
    for eq in ['First', 'Second']:
        num_terms = ''
        while not num_terms.strip().isdigit():
            num_terms = input("Enter the number of terms for {} Equation: ".format(eq))
            print("\n")
        for i in range(1, int(num_terms)+1):
            co_eff = ''
            power = ''
            while not co_eff.strip().isdigit():
                co_eff = input("Enter the cofficient of {}{} term: ".format(i, ("th" if 4 <= i % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(i % 10, "th"))))
            while not power.strip().isdigit():
                power = input("Enter the power of  x for {}{} term: ".format(i, ("th" if 4 <= i % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(i % 10, "th"))))
            print("\n{}x^{}\n".format(co_eff, power))
            if eq == "First":
                equation1 = add_new_node(equation1, int(co_eff), int(power))
            else:
                equation2 = add_new_node(equation2, int(co_eff), int(power))
    return


# Display both the equations
def display_polynomial():
    global equation2
    global equation1
    if equation1 is None or equation2 is None:
        print("\n\n----------------------------------------------------------\n")
        print("No Polynomial Equations are created. Please select option one to create two equations\n")
        print("\n----------------------------------------------------------\n\n")
        return
    print("\n----EQUATION 1----\n")
    print_polynomial(equation1)
    print("\n------------------\n\n")

    print("\n----EQUATION 2----\n")
    print_polynomial(equation2)
    print("\n------------------\n\n")
    return


# Add node at end of Double Linked List
def add_new_node(start, coeff, power):
    # Create New Node
    new_node = Node()
    new_node.coeff = coeff
    new_node.power = power
    new_node.next = None
    new_node.prev = None

    # If this is first Node then return
    if start is None:
        return new_node

    # If the equation list has nodes
    pointer = start
    while pointer.next is not None:
        pointer = pointer.next
    pointer.next = new_node
    new_node.prev = pointer
    return start


# Function To Display The Linked list
def print_polynomial(pointer):
    while pointer is not None:
        if int(pointer.power) == 0:
            print("{}".format(pointer.coeff), end=" ")
        else:
            print("{}x^{}".format(pointer.coeff, pointer.power), end=" ")
        if pointer.next is not None and pointer.next.coeff >= 0:
            print('+', end=" ")
        pointer = pointer.next


# If 2 nodes have same coeff, then we need to add them. Example 2x^2 + 3x^2 = 5x^2
def merge_same_coeff(start):
    pointer2 = None
    pointer1 = start

    # Keep 2 pointer and go through all the elements to find duplicates
    while pointer1 is not None and pointer1.next is not None:
        pointer2 = pointer1
        while pointer2.next is not None:
            # add the coeff of 2 element if their powers are same
            if pointer1.power == pointer2.next.power:
                pointer1.coeff = pointer1.coeff + pointer2.next.coeff
                pointer2.next = pointer2.next.next
                if pointer2.next is not None:
                    pointer2.next.prev = pointer2.prev
            else:
                pointer2 = pointer2.next
        pointer1 = pointer1.next

# Function two Multiply two polynomial Numbers
def multiply_polynomial():
    # Create two pointer and store the
    # address of 1st and 2nd polynomials
    if equation1 is None or equation2 is None:
        print("\n\n----------------------------------------------------------\n")
        print("No Polynomial Equations are created. Please select option one to create two equations\n")
        print("\n----------------------------------------------------------\n\n")
        return
    pointer1 = equation1
    pointer2 = equation2
    equation3 = None

    while pointer1 is not None:
        while pointer2 is not None:
            # Multiply the coefficient of both
            # polynomials and store it in coeff
            coeff = int(pointer1.coeff) * int(pointer2.coeff)
            power = int(pointer1.power) + int(pointer2.power)
            equation3 = add_new_node(equation3, int(coeff), int(power))
            pointer2 = pointer2.next
        pointer2 = equation2
        pointer1 = pointer1.next
    print("\n----- Multiplication Results Before Merging Similar Co-efficients ----- \n")
    print_polynomial(equation3)
    print("\n\n\n------------------ Final Multiplication Results ------------------- \n")
    merge_same_coeff(equation3)
    print_polynomial(equation3)
    print("\n----------------------------------------------------------------------- \n\n\n")
    return


# Function two add two polynomial Numbers
def add_polynomial():
    # Create two pointer and store the
    # address of 1st and 2nd polynomials
    if equation1 is None or equation2 is None:
        print("\n\n----------------------------------------------------------\n")
        print("No Polynomial Equations are created. Please select option one to create two equations\n")
        print("\n----------------------------------------------------------\n\n")
        return
    pointer1 = equation1
    pointer2 = equation2
    equation3 = None

    while pointer1 is not None:
        equation3 = add_new_node(equation3, int(pointer1.coeff), int(pointer1.power))
        pointer1 = pointer1.next

    while pointer2 is not None:
        equation3 = add_new_node(equation3, int(pointer2.coeff), int(pointer2.power))
        pointer2 = pointer2.next

    print("\n----- Addition Results Before Merging Similar Co-efficients ----- \n")
    print_polynomial(equation3)
    print("\n\n\n------------------ Final Addition Results  -------------------- \n")
    merge_same_coeff(equation3)
    print_polynomial(equation3)
    print("\n----------------------------------------------------------------------- \n\n\n")


# Main
if __name__ == '__main__':

    equation1 = None
    equation2 = None

    while True:
        response = None
        while response not in {'1', '2', '3', '4', '5'}:
            input_msg = """
Enter your option from the below list of permitted options(1/2/3/4/5)
1. Create_Polynomial_List 
2. Display_Polynomial
3. ADD_Polynomials
4. Multiply
5. Quit
Your Choice: """
            response = input(input_msg)
        print("Response is {}".format(response))

        if response == "1":
            equation1 = None
            equation2 = None
            create_polynomial_list()
            display_polynomial()
        if response == "2":
            display_polynomial()
        if response == "3":
            add_polynomial()
        if response == "4":
            multiply_polynomial()
        if response == "5":
            break
