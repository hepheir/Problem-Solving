def make_vector(src, dst):
    return [x[1]-x[0] for x in zip(src,dst)]

if __name__ == "__main__":
    P1 = tuple(map(int, input().split()))
    P2 = tuple(map(int, input().split()))
    P3 = tuple(map(int, input().split()))

    v1 = make_vector(P1, P2)
    v2 = make_vector(P2, P3)

    z = v1[0]*v2[1] - v1[1]*v2[0]

    if z == 0:
        print(0)
    elif z > 0:
        print(1)
    else:
        print(-1)