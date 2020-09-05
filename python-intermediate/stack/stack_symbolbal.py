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

def checkSymbolBalance(input):
    symbolstack = Stack()
    balanced =0
    topSymbol = None
    for symbols in input:
        if symbols in ["{","(","["]:
            symbolstack.push(symbols)
        else:
            if symbolstack.isEmpty() == 0:
                balanced = 0
                return balanced
            else:
                topSymbol = symbolstack.pop()
                if matches(topSymbol, symbols): 
                    balanced = 1
                else:
                    balanced = 0

    if symbolstack.isEmpty() == None:
        balanced = 1
        print(" Symbols are perfectly matched")
    else:
        balanced = 0
        print(" Symbols are not matched")

    return balanced

print(checkSymbolBalance("{{([][])}()}(){}[]"))
print(checkSymbolBalance("{{([][])}(){"))
