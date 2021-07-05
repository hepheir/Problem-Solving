import sys
sys.setrecursionlimit(10**5)

import math
import fractions

MAX_t = 25
DEFAULT_COEFF_SIZE = 32

class CoefficienceSequence:
    def copy(self):
        coeff = CoefficienceSequence(self.size)
        coeff.list = self.list.copy()
        return coeff

    def __init__(self, size=DEFAULT_COEFF_SIZE):
        self.list = [fractions.Fraction(0) for _ in range(size)]
        self.size = size
    
    def __add__(self, coeff):
        new_coeff = self.copy()
        for idx in range(coeff.size):
            new_coeff.list[idx] += coeff[idx]
        return new_coeff
    
    def __sub__(self, coeff):
        new_coeff = self.copy()
        for idx in range(coeff.size):
            new_coeff.list[idx] -= coeff[idx]
        return new_coeff
    
    def __mul__(self, num):
        new_coeff = self.copy()
        for idx in range(self.size):
            new_coeff.list[idx] *= num
        return new_coeff
    
    def __truediv__(self, num):
        new_coeff = self.copy()
        for idx in range(self.size):
            new_coeff.list[idx] /= num
        return new_coeff
    
    def __getitem__(self, index):
        return self.list[index]
    
    def __setitem__(self, index, value):
        self.list[index] = value
    
    def __str__(self):
        def a(frac):
            if frac.denominator == 1:
                return str(frac.numerator)
            else:
                return f'{frac.numerator}/{frac.denominator}'
        return f'[{", ".join(list(map(a, self.list)))}]'
    
    def __repr__(self):
        return self.__str__()

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def polynomial_x_plus_1(k):
    """(x+1)^k의 곱셈 공식을 구한다."""
    half = [nCr(k, r) for r in range(k//2 + 1)]
    if k % 2:
        # Odd degree
        return half+half[::-1]
    else:
        # Even degree
        return half[:-1]+half[::-1]

__sigma_k_powered_Cached = [None] * (MAX_t+2)

def sigma_k_powered(a):
    """sigma(k=1~n: k^a) 의 n에 관한 식을 구한다.
    참고문서(자연수 거듭 제곱의 합): https://blog.naver.com/PostView.nhn?blogId=dalsapcho&logNo=20141141955"""
    if __sigma_k_powered_Cached[a] is None:
        coeff = CoefficienceSequence()
        if a == 0:
            coeff[1] = fractions.Fraction(1)
        elif a == 1:
            coeff[1] = fractions.Fraction(1,2)
            coeff[2] = fractions.Fraction(1,2)
        else:
            poly = polynomial_x_plus_1(a+1)
            lp = [0]+poly[1:] # 전개할 좌항의 n의 계수들
            rp = poly[:-2] # 개별 수열의 합을 구할 우항의 계수들
            cs = poly[-2] # k^a 자신의 계수
            for deg, cof in enumerate(lp):
                coeff[deg] += cof
            for deg, cof in enumerate(rp):
                coeff -= sigma_k_powered(deg) * cof
            coeff /= cs
        __sigma_k_powered_Cached[a] = coeff
    return __sigma_k_powered_Cached[a]

def Sn(t, c):
    coeff = CoefficienceSequence()
    for a in range(t+1):
        coeff += sigma_k_powered(a) * c[a]
    coeff[0] += c[0] # k가 0부터 시작하므로 추가 (0^0 x c0) 
    return coeff

def testcase():
    raw = list(map(int, input().split()))
    t, c = raw[0], raw[1:]
    answer = sum([abs(frac.numerator) for frac in Sn(t, c)])
    print(answer)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        testcase()