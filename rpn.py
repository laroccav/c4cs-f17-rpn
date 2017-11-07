#!/usr/bin/env python3
import operator
import readline
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.floordiv,
	'%': operator.mod,
	'^': operator.pow
}

def calculate(arg):
	stack = list()
	in_string = arg
	for token in arg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
		# print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	for token2 in in_string.split():
		try:
			if int(token2) < 0:
				print(Back.RED + token2 + Style.RESET_ALL, end=' ')
			else:
				print(token2, end=' ')
		except ValueError:
			print(Fore.GREEN + Style.BRIGHT + token2 + Style.RESET_ALL, end=' ')
	print()
	return stack.pop()

def main():
    while True:
        print ("Result: ", calculate(input("rpn calc> ")))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
