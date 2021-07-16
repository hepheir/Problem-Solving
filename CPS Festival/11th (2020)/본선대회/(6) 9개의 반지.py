from fractions import Fraction, gcd
from functools import reduce

def solve(total_water):
  cases = 0
  total_water
  for w1 in range(total_water):
    if w1 >= 300: continue
    stack1 = [w1]
    for w2 in range(total_water - sum(stack1)):
      if w2 >= 300: continue
      if w2 in stack1: continue
      stack2 = stack1 + [w2]
      for w3 in range(total_water - sum(stack2)):
        if w3 >= 300: continue
        if w3 in stack2: continue
        stack3 = stack2 + [w3]
        for w4 in range(total_water - sum(stack3)):
          if w4 >= 300: continue
          if w4 in stack3: continue
          stack4 = stack3 + [w4]
          for w5 in range(total_water - sum(stack4)):
            if w5 >= 300: continue
            if w5 in stack4: continue
            stack5 = stack4 + [w5]
            for w6 in range(total_water - sum(stack5)):
              if w6 >= 300: continue
              if w6 in stack5: continue
              stack6 = stack5 + [w6]
              for w7 in range(total_water - sum(stack6)):
                if w7 >= 300: continue
                if w7 in stack6: continue
                stack7 = stack6 + [w7]
                for w8 in range(total_water - sum(stack7)):
                  if w8 >= 300: continue
                  if w8 in stack7: continue
                  stack8 = stack7 + [w8]

                  w9 = total_water - sum(stack8)
                  if w9 >= 300: continue
                  if w9 in stack8: continue
                  stack9 = stack8 + [w9]

                  W = stack9
                  if checkValid(total_water, W):
                    print('\r가능한 경우: ', W)

def isPrime(x:int):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

def checkValid(total_water, W:list):
  total_gold = total_water
  water_per_person = Fraction(total_water, 10)
  W_give = [Fraction(w) - water_per_person for w in W] # 각자 사우론에게 준 물의 양
  total_give = sum(W_give)
  G = [(w / total_give * total_gold) for w in W_give]
  
  if sum(W) != sum(G):
    return False
  if len(set(G) - set(W)) != 9:
    return False
  
  n_of_not_primes = 0
  for x in W + G:
    if not isPrime(x):
      n_of_not_primes += 1
    if n_of_not_primes > 1:
      return False

  return True

if __name__ == '__main__':
  for total_water in range(1000):
    solve(total_water)
