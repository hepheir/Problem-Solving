a, b=map(int,input().split())
large=(a/2)+(b/2)
small=(a/2)-(b/2)
if (a/2)+(b/2)<50 or (a/2)-(b/2)>0:
    if b/2 - int(b/2) == 0:
        large=int(large)
        small=int(small)
        print(large, small)
    else:
        print('impossible')
else:
    print('impossible')
