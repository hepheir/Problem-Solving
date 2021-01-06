from fractions import Fraction as Frac

a,b,c,d,e,f = map(int, input().split())

x = (Frac(c, b) - Frac(f, e)) / (Frac(a, b) - Frac(d, e))
y = Frac(c, b) - Frac(a, b) * x

print(x, y)