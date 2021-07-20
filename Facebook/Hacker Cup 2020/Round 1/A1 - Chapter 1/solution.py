import sys
import functools

file_name = 'Round 1/A1 - Chapter 1/data/perimetric_chapter_1_input.txt'
sys.stdin = open(file_name, 'r')
sys.stdout = open(file_name.replace('input','output'), 'w')
input = sys.stdin.readline
mod = int(1e9+7)

def modded_mult(a,b):
    return (a * b) % mod

def solve(floorplan_num):
    N, K, W = map(int, input().split())
    L = list(map(int, input().split())) # N-length
    Al,Bl,Cl,Dl = map(int, input().split())
    H = list(map(int, input().split())) # K-length
    Ah,Bh,Ch,Dh = map(int, input().split())
    for i in range(K, N):
        Li = ((Al*L[i-2]+Bl*L[i-1]+Cl) % Dl)+1
        Hi = ((Ah*H[i-2]+Bh*H[i-1]+Ch) % Dh)+1
        L.append(Li)
        H.append(Hi)
    P = []
    for i in range(N):
        if i == 0:
            Pi = 2*(W+H[i])
        elif L[i]-L[i-1] > W: # if the last two rooms do not overlap
            Pi = P[i-1] + 2*(W+H[i])
        elif H[i] <= H[i-1]:
            w = L[i]-L[i-1]
            Pi = P[i-1] + 2*w
        else:
            mh = H[i-1]
            for k in range(i-1, -1, -1):
                if L[k]+W < L[i]:
                    break
                else:
                    mh = max(mh, H[k])
            if H[i] <= mh:
                w = L[i]-L[i-1]
                Pi = P[i-1] + 2*w
            else:
                w = L[i]-L[i-1]
                h = H[i]-mh
                Pi = P[i-1] + 2*(w+h)
        P.append(Pi)
    return functools.reduce(modded_mult, P)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        answer = solve(t)
        print(f'Case #{t}: {answer}')