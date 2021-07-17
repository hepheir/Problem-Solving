import operator
import re
import functools

expression = input()

# 숫자 앞의 0을 제거
expression = re.sub(r'\+0+', '+', expression)
expression = re.sub(r'-0+', '-', expression)

expressions = expression.split('-')
expressions = list(map(eval, expressions))
print(functools.reduce(operator.sub, expressions))