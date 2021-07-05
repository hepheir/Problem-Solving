A = int(input())
B = int(input())
C = int(input())
calced_string = str(A*B*C)
for i_str in '0123456789':
    print(calced_string.count(i_str))