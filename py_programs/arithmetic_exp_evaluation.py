"""
author: Sunil K B

description:
Develop a python application to implement the following :
Input a fully parenthesized arithmetic expression and converts it to a binary expression tree.
Your program should display the tree in some way and also print the value associated with the root.
For an additional challenge, allow for the leaves to store variables of the form x1, x2, X3, and so on,
which are initially 0 and which can be updated interactively by your program,
with the corresponding update in the printed value of the root of the expression tree.

usage:
python3 DSA_2.py
"""

from __future__ import print_function
import re
import sys
if sys.version_info < (3, 0, 0):
    print(__file__ + ' requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating. Run - python3 '+__file__))
    sys.exit(1)


def print_tree(root, space):
    space_tab = 5
    if root == None:
        return
    space += space_tab

    # Process right child first
    print_tree(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(space_tab, space):
        print(end=" ")
    print(root.data)

    # Process left child
    print_tree(root.left, space)


# Wrapper over print_tree()
def display_tree(root):
    print_tree(root, 0)


# Base node class has attributes for data, pointer to left tree and pointer to right tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Stack class which has basic stack functionalities like push, pop, get top element and get size of stack
class Stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        if len(self.arr):
            return self.arr.pop(-1)

    def top(self):
        if len(self.arr):
            return self.arr[-1]

    def size(self):
        return len(self.arr)


# Class for Infix to Postfix conversion
class InfixToPostfix:
    # Set precedence based on match arithmetic
    precedence = {'*': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 1}

    def __init__(self):
        self.items = []
        self.size = -1

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size -= 1
            return self.items.pop()

    def isempty(self):
        if self.size == -1:
            return True
        else:
            return False

    def peek(self):
        if self.isempty():
            return False
        else:
            return self.items[self.size]

    def convert_infix_to_postfix(self, expr):
        postfix = ""
        for i in re.findall('[+-/*//()]|\d+', expr):
            if re.match('^[a-zA-Z0-9_]+$', i):
                postfix = postfix + " " + i
            elif i in '+-*/':
                while len(self.items) and self.precedence[i] <= self.precedence[self.peek()]:
                    postfix = postfix + " " + self.pop()
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o = self.pop()
                while o != '(':
                    postfix += o
                    o = self.pop()
        while len(self.items):
            if self.peek() == '(':
                self.pop()
            else:
                postfix = postfix + " " + self.pop()
        return postfix


# expression tree class
class ExpTree:
    def __init__(self, postfix_exp):
        self.str_len = len(re.findall('[+-/*//()]|\d+', postfix_exp))
        self.count = 0
        self.pos_arr = []
        self.exp = postfix_exp
        self.root = None
        self.create_tree(self.exp)

    def is_operator(self, char):
        optr = ["+", "-", "*", "/"]
        if char in optr:
            return True
        return False

    def create_tree(self, expr):
        exp = re.findall('[+-/*//()]|\d+', expr)
        s = Stack()
        level = 0
        self.root = Node(exp[-1])
        self.pos_arr.insert(self.count, "T")
        self.count = self.count + 1
        self.str_len = self.str_len - 1
        s.push(self.root)
        for i in reversed(exp[0:-1]):
            curr_node = s.top()
            if not curr_node.right:
                temp = Node(i)
                curr_node.right = temp
                if self.is_operator(i):
                    s.push(temp)
                    level = level + 1
                self.pos_arr.insert(self.count, "R")
                self.count += 1
            elif not curr_node.left:
                temp = Node(i)
                curr_node.left = temp
                s.pop()
                if self.is_operator(i):
                    s.push(temp)
                    level = level + 1
                self.pos_arr.insert(self.count, "L")
                self.count += 1


class EvaluatePostfix:
    def __init__(self):
        self.items=[]
        self.size=-1

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)
        self.size+=1

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]

    def evaluate(self, expr):
        for i in re.findall('[+-/*//()]|\d+', expr):
            if i.strip().isdigit():
                self.push(i)
            else:
                op1 = self.pop()
                op2 = self.pop()
                outcome = self.calculate(op2, op1, i)
                self.push(outcome)
        return self.pop()

    def calculate(self, op2, op1, i):
        if i == '*':
            return int(op2)*int(op1)
        elif i == '/':
            return int(op2)/int(op1)
        elif i == '+':
            return int(op2)+int(op1)
        elif i == '-':
            return int(op2)-int(op1)


if __name__ == "__main__":

    # Create a Infix to Postfix object
    inf_post_obj = InfixToPostfix()
    expr = ''
    while not re.match(r'^[-+*\/0-9\(\)\s]+$', expr):
        expr = input('Enter a valid arithmetic expression (Allowed Operators are + - * /): ')
        if len(re.findall('[+-/*//()]|\d+', expr)) % 2 == 0:
            print("Wrong Expression. Try again")
            expr = ''
        expr = re.sub(r'[ \n]+', "", expr)

    result = inf_post_obj.convert_infix_to_postfix(expr)

    if result:
        print("\n Infix Expression is {}\n".format(expr))
        print("\n Postfix Expression is {}\n".format(result))

    etree = ExpTree(result)
    display_tree(etree.root)

    postfix_obj = EvaluatePostfix()
    value = postfix_obj.evaluate(result)
    print("Final Result of {} is {}".format(expr, value))
