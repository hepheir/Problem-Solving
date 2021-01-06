from fractions import Fraction as Frac

a, b, c, d, e, f = map(int, input().split())

if a == 0:
    y = Frac(c, b)
    x = Frac(f, d) - Frac(e, d) * y
elif b == 0:
    x = Frac(c, a)
    y = Frac(f, e) - Frac(d, e) * x
elif d == 0:
    y = Frac(f, e)
    x = Frac(c, a) - Frac(b, a) * y
elif e == 0:
    x = Frac(f, d)
    y = Frac(c, b) - Frac(a, b) * x
else:
    x = (Frac(c, b) - Frac(f, e)) / (Frac(a, b) - Frac(d, e))
    y = Frac(c, b) - Frac(a, b) * x

print(x, y)
