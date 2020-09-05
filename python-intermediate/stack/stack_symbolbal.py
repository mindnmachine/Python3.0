import sys
import re 
sys.path.append(".")
from stack_class import Stack 

def matches(topSymbol, symbols):
    if topSymbol == "{" and symbols =="}":
        return 1
    elif topSymbol == "(" and symbols ==")":
            return 1
    elif topSymbol == "[" and symbols =="]" : 
           return 1
    else:
       return 0

def errorHandling(balanced):
    balanced = 0

def checkSymbolBalance(input):
    symbolstack = Stack()
    balanced =0
    topSymbol = None
    for symbols in input:
        if symbols in ["{","(","["]:
            symbolstack.push(symbols)
        else:
            if symbolstack.isEmpty() == 0:
                return errorHandling(balanced)
            else:
                topSymbol = symbolstack.pop()
                if topSymbol == 0:
                   errorHandling(balanced)
                   break

                if matches(topSymbol, symbols): 
                    balanced = 1
                else:
                    balanced = 0

    if symbolstack.isEmpty() == None and topSymbol != 0:
        balanced = 1
        print(" Symbols are perfectly matched")
    else:
        balanced = 0
        print(" Symbols are not matched")

    return balanced

string1 ="{{{([][])}()}(){}[]}"
string2 = "{{([][])}(){"
string3 = "{{}}(([][]))()"

print("String passed is ",string1)
print(checkSymbolBalance(string1))

print("String passed is ",string2)
print(checkSymbolBalance(string2))

print("String passed is ",string3)
print(checkSymbolBalance(string3))
