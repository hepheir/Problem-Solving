import sys
input = sys.stdin.readline

class Room:
    def __init__(self, x, y):
        self.paintable = True
        self.connect = []

def make(building:dict, x, y, n_rows):
    new_room = Room(x, y)
    building[x,y] = new_room
    if not (x % 2): # if is Inverted Triangle,
        new_room.connect.append(make(building, x-1, y, n_rows))
        new_room.connect.append(make(building, x+1, y, n_rows))
    elif y < n_rows:
        new_room.connect.append(make(building, x+1, y+1, n_rows))
    return new_room

def solve(side_length:int, alma_starting_room:(int,int), bert_starting_room:(int,int), rooms_under_construction:[(int,int)]):
    # Greedy?
    # init
    museum = {}
    scores = [1, 1]
    make(museum, 1, 1, side_length)
    for x, y in rooms_under_construction:
        museum[x,y].paintable = False
    museum[alma_starting_room].paintable = False
    museum[bert_starting_room].paintable = False
    alma_pos = alma_starting_room
    bert_pos = bert_starting_room
    
    return None # TODO

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        S, RA, PA, RB, PB, C = map(int, input().split()) # Side length of the mueum
        R, P = [], []
        for c in range(C):
            Ri, Pi = map(int, input().split())
            R.append(Ri)
            P.append(Pi)
        ans = solve(S, (RA, PA), (RB, PB), list(zip(R, P)))
        print('Case #{0}: {1}'.format(t+1, ans))