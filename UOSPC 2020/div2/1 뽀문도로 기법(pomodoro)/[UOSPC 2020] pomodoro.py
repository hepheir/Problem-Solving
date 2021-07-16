m = int(input())
a, b = map(int, input().split())

cycle = m // (a + b)
mod = m % (a + b)

print(cycle*a + min(mod, a))