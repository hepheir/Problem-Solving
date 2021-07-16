def solution(n, k, cmd_list):
    prev = [i for i in range(-1, n-1)]
    next = [i for i in range(1, n+1)]
    is_deleted = [False] * n
    trash_bin = []
    selected = k
    for cmd in cmd_list:
        if cmd.startswith('U'):
            x = int(cmd.split()[1])
            for _ in range(x):
                selected = prev[selected]

        elif cmd.startswith('D'):
            x = int(cmd.split()[1])
            for _ in range(x):
                selected = next[selected]

        elif cmd.startswith('C'):
            to_delete = selected
            is_deleted[to_delete] = True
            trash_bin.append(to_delete)
            if prev[to_delete] >= 0:
                next[prev[to_delete]] = next[to_delete]
            if next[to_delete] < n:
                prev[next[to_delete]] = prev[to_delete]
            #
            try:
                selected = next[to_delete]
            except
            if to_delete == n-1:
                selected = prev[to_delete]
            elif is_deleted[next[to_delete]]:
                selected = prev[to_delete]
            else:


        elif cmd.startswith('Z'):
            deleted = trash_bin.pop()
            is_deleted[deleted] = False
            if prev[deleted] >= 0:
                next[prev[deleted]] = deleted
            if next[deleted] < n:
                prev[next[deleted]] = deleted

    return ''.join([('X' if node else 'O') for node in is_deleted])


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))