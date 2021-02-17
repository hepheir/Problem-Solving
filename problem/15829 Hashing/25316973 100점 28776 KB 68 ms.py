r=31
m=1234567891
input()
print(sum((ord(c)-96)*pow(r,i,m)for i,c in enumerate(input()))%m)