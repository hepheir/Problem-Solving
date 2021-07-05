def solve(R, S):
    P = ''
    for c in S:
        P += c * R
    return P

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, S = input().split()
        R = int(R)
        P = solve(R, S)
        print(P)