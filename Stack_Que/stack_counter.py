def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 0  

def infix_to_postfix(expression):
    opstack = []       
    outstack = []     

    tokens = list(expression.replace(" ", ""))  

    for token in tokens:
        if token.isnumeric():
            outstack.append(token)
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            while opstack and opstack[-1] != '(':
                outstack.append(opstack.pop())
            opstack.pop()       
        else:  
            while opstack and precedence(opstack[-1]) >= precedence(token):
                outstack.append(opstack.pop())
            opstack.append(token)

    while opstack:
        outstack.append(opstack.pop())

    return ' '.join(outstack)

expr = "3 + 4 * 2 / ( 1 - 5 )"
result = infix_to_postfix(expr)
print("후위표기식:", result)
