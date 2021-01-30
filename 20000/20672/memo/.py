import sys
import math
import collections
import functools

sys.setrecursionlimit(10**6)

# WARNING THIS IS FOR DEBUGGING
sys.stdin = open('20000/20672/data/boj.sait2000.in', 'r')

MOD = 10**9+7

CHECKED = True
NOT_CHECKED = False

CLOSED = True
NOT_CLOSED = False
class Tree:
    def __init__(self):
        N = int(sys.stdin.readline())
        self.g = [0, *map(int, sys.stdin.readline().split())]
        self.graph = [list() for _ in range(N+1)]
        self.parent = [n for n in range(N+1)]
        self.answer = [0] * (N+1)
        for n in range(N-1):
            u, v = map(int, sys.stdin.readline().split())
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.make_subtree(1)
        # self.bfs(1)

        first_child = next(self.get_children(1))
        self.dfs(first_child, CHECKED, NOT_CLOSED, self.g[1])
        self.dfs(first_child, NOT_CHECKED, NOT_CLOSED, self.g[1])

    def make_subtree(self, node):
        for child in self.get_children(node):
            self.set_parent(child, node)
            self.make_subtree(child)

    def is_root(self, node):
        return node == self.get_parent(node)
    
    def is_leaf(self, node):
        return (self.is_root(node) == False) and (len(self.graph[node]) == 1)
    
    def get_parent(self, node):
        return self.parent[node]
    
    def set_parent(self, node, parent):
        self.parent[node] = parent

    def get_children(self, node):
        for child in self.graph[node]:
            if child != self.get_parent(node):
                yield child

    def get_siblings(self, node):
        for sibling in self.get_children(self.get_parent(node)):
            if sibling != node:
                yield sibling

    @functools.cache
    def estimate_othercases(self, node, is_checked, is_closed):
        if is_checked:
            retval = 1
            for child in self.get_children(node):
                retval *= self.estimate_othercases(child, CHECKED, NOT_CLOSED) \
                        + self.estimate_othercases(child, NOT_CHECKED, CLOSED)
            return retval
        elif is_closed:
            return 1
        else:
            retval = 0
            for child in self.get_children(node):
                retval += self.estimate_othercases(child, NOT_CHECKED, NOT_CLOSED)
            return retval
    
    @functools.cache
    def othercases(self, child, is_parent_checked):
        if is_parent_checked:
            retval = 1
            for sibling in self.get_siblings(child):
                retval *= self.estimate_othercases(sibling, CHECKED, NOT_CLOSED) \
                        + self.estimate_othercases(sibling, NOT_CHECKED, CLOSED)
            return retval
        else:
            retval = 0
            for sibling in self.get_siblings(child):
                retval += self.estimate_othercases(sibling, CHECKED, NOT_CLOSED)
            return retval

    def dfs(self, node, is_checked, is_closed, cheatkey):
        if is_checked == CHECKED: # (?) -> ... -> (o) -> opened
            assert is_closed == NOT_CLOSED
            cheatkey = math.gcd(self.g[node], cheatkey)
            for child in self.get_children(node):
                for _ in range(self.othercases(child, is_parent_checked=CHECKED)):
                    self.dfs(child, CHECKED, NOT_CLOSED, cheatkey)
                    self.dfs(child, NOT_CHECKED, CLOSED, cheatkey)

        elif is_closed == CLOSED: # (o) -> ... -> (x) -> closed
            for child in self.get_children(node):
                self.dfs(child, NOT_CHECKED, CLOSED, cheatkey)

        else: # (x) -> ... -> (x) -> opened
            for child in self.get_children(node):
                for _ in range(self.othercases(child, is_parent_checked=NOT_CHECKED)):
                    self.dfs(child, NOT_CHECKED, CLOSED, cheatkey)
                self.dfs(child, CHECKED, NOT_CLOSED, cheatkey)
                self.dfs(child, NOT_CHECKED, NOT_CLOSED, cheatkey)

        if self.is_leaf(node):
            self.answer[node] += cheatkey

    
    def bfs(self, root):
        first_child = next(self.get_children(root))
        deque = collections.deque()
        deque.append((first_child, CHECKED, NOT_CLOSED, self.g[root]))
        deque.append((first_child, NOT_CHECKED, NOT_CLOSED, self.g[root]))
        while deque:
            node, is_checked, is_closed, cheatkey = deque.popleft()

            if is_checked == CHECKED: # (?) -> ... -> (o) -> opened
                assert is_closed == NOT_CLOSED
                cheatkey = math.gcd(self.g[node], cheatkey)
                for child in self.get_children(node):
                    for _ in range(self.othercases(child, is_parent_checked=CHECKED)):
                        deque.append((child, CHECKED, NOT_CLOSED, cheatkey))
                        deque.append((child, NOT_CHECKED, CLOSED, cheatkey))

            elif is_closed == CLOSED: # (o) -> ... -> (x) -> closed
                for child in self.get_children(node):
                    deque.append((child, NOT_CHECKED, CLOSED, cheatkey))

            else: # (x) -> ... -> (x) -> opened
                for child in self.get_children(node):
                    for _ in range(self.othercases(child, is_parent_checked=NOT_CHECKED)):
                        deque.append((child, NOT_CHECKED, CLOSED, cheatkey))
                    deque.append((child, CHECKED, NOT_CLOSED, cheatkey))
                    deque.append((child, NOT_CHECKED, NOT_CLOSED, cheatkey))

            if self.is_leaf(node):
                self.answer[node] += cheatkey


print(*(ans % MOD for ans in Tree().answer if ans))