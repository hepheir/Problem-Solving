import operator
import functools

expression = input()

# eval 시 SyntaxError 방지 처리
parsed_expr = []
buffer = ''
for c in expression:
    if c in '+-':
        parsed_expr.append(str(int(buffer)))
        parsed_expr.append(c)
        buffer = ''
    else:
        buffer += c
parsed_expr.append(str(int(buffer)))
expression = ''.join(parsed_expr)

print(functools.reduce(operator.sub, list(map(eval, expression.split('-')))))