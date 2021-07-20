import sys
import functools

file_name = 'Round 1/A2 - Chapter 2/data/perimetric_chapter_2_validation_input.txt'
sys.stdin = open(file_name, 'r')
sys.stdout = open(file_name.replace('input','output'), 'w')
input = sys.stdin.readline
mod = int(1e9+7)

def modded_mult(a,b):
    return (a * b) % mod

def intersects(Ax1,Ax2,Bx1,Bx2):
    return Ax1 <= Bx2 and Bx1 <= Ax2

def P_iter():
    Pi_1 = 0
    lines = []
    for i in range(N):
        Pi = Pi_1 + 2*(W[i]+H[i])
        #
        x1, x2 = L[i], L[i]+W[i]
        for j in range(len(lines)-1, 0, -2):
            x3, x4 = lines[j-1], lines[j]
            if x4 < x1: continue
            if x2 < x3: break
            if intersects(x1,x2,x3,x4):
                Pi -= 2 * (H[i] + min(x2,x4)-max(x1,x3))
                x1 = min(x1,x3)
                x2 = max(x2,x4)
                lines.remove(x3)
                lines.remove(x4)
        lines += [x1, x2]
        lines = sorted(lines)
        Pi_1 = Pi
        yield Pi

def solve(floorplan_num):
    global N, K, L, W, H
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    Al,Bl,Cl,Dl = map(int, input().split())
    W = list(map(int, input().split()))
    Aw,Bw,Cw,Dw = map(int, input().split())
    H = list(map(int, input().split()))
    Ah,Bh,Ch,Dh = map(int, input().split())
    # Fill values
    for i in range(K, N):
            Li = ((Al*L[i-2]+Bl*L[i-1]+Cl) % Dl)+1
            Wi = ((Aw*W[i-2]+Bw*W[i-1]+Cw) % Dw)+1
            Hi = ((Ah*H[i-2]+Bh*H[i-1]+Ch) % Dh)+1
            L.append(Li)
            W.append(Wi)
            H.append(Hi)
    return functools.reduce(modded_mult, P_iter())

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        answer = solve(t)
        print(f'Case #{t}: {answer}')