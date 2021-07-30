# 문제

-   **제목**: 바이러스 밀폐
-   **배점**: 20점

# 답하기

## (1) 모든 연구실을 밀폐하기 위하여 지나가는 길을 밀폐경로라고 합니다. 밀폐경로는 몇 가지가 있습니까? 경로가 없으면 0을 적습니다.

0.

경로가 없다.

## (2) 경로를 선으로 나타냅니다. 여러 가지 경로가 있으면 각각 독립하여 그립니다.

경로가 없습니다.

## (3) 경로를 찾은 방법을 설명합니다.

### 풀이에 사용한 방법

놓치는 경우의 수 하나 없이 모든 경우의 수를 찾아내기 위해,

간단한 Python 프로그램을 작성하였다.

### 사용한 알고리즘

사용한 알고리즘은 너비우선탐색(BFS)의 응용이며, 다음과 같은 절차로 탐색한다.

1. 초기 위치는 입구가 있는 방이다.

2. 현재의 방에서 갈 수 있는 가장 가까운 방(= 연결되어 있는 방) 중, 아직 방문하지 않은 방을 선택한다.

3. 갈 수 있는 방이 더 이상 없을 때 까지 2번 동작을 반복한다.

4. 마지막으로 위치했던 방이 출구가 있는 방인 경우, 지나온 경로를 출력한다.

### 결론

#### 밀폐경로

입구로 들어가 출구로 나오는 해밀턴 경로,
즉 밀폐경로는 존재하지 않는다.

#### 해밀턴 경로

그러나, 입구로 들어가고 반드시 출구로 나오지 않아도 되는,
단순 해밀턴 경로는 생각보다 꽤 존재한다.

좌상단으로 들어가는 경우, 총 52가지의 해밀턴 경로가 존재한다. [하단 코드 실행결과 참고]
#### 이 들의 관계

해밀턴 경로의 경우, 좌상단으로 들어가 어디서 경로가 끝나는지를 분석해 보면 특정한 성질이 있다.
끝나는 방의 (x좌표의 값) + (y좌표의 값)이 모두 홀수라는 것이다.

본 지문에서 밀폐경로를 찾을 수 없었던 이유는,
좌상단으로 들어가 경로가 종료되어야 할 출구의 (x좌표의 값) + (y좌표의 값)이 3 + 3 = 6으로,
짝수였기 때문이다.

왜이러한 결과가 나오는지는 후속적인 연구를 통해 알아보면 좋을 것 같다.

### 사용한 코드와 실행결과

<details>
<summary>코드 보기</summary>

```python
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque, Generator, List


@dataclass
class Point:
    x: int
    y: int


class Room(Point):
    laboratory: Laboratory

    def __init__(self, laboratory: laboratory, x: int, y: int) -> None:
        super().__init__(x, y)
        self.laboratory = laboratory

    def _get_room(self, x: int, y: int) -> Room | None:
        """이 방과 같은 실험실에 있는 `x`, `y`번 방을 반환합니다.

        만약, 해당 방이 방문 불가능한 방이라면, `None`을 반환합니다.
        """
        width = self.laboratory.width
        height = self.laboratory.height
        if (0 <= x < width) and (0 <= y < height):
            return self.laboratory.rooms[y][x]
        else:
            return None

    @property
    def left(self) -> Room:
        return self._get_room(self.x-1, self.y)

    @property
    def right(self) -> Room:
        return self._get_room(self.x+1, self.y)

    @property
    def up(self) -> Room:
        return self._get_room(self.x, self.y-1)

    @property
    def down(self) -> Room:
        return self._get_room(self.x, self.y+1)


class Laboratory:
    def __init__(self,
                 width: int,
                 height: int,
                 entrance_point: Point,
                 exit_point: Point) -> None:
        self.width = width
        self.height = height
        self._rooms = [[Room(self, x, y) for x in range(width)]
                       for y in range(height)]
        self._entrance_point = entrance_point
        self._exit_point = exit_point

    @property
    def size(self) -> int:
        return self.width * self.height

    @property
    def rooms(self) -> List[List[Room]]:
        return self._rooms

    @property
    def entrance(self) -> Room:
        return self.rooms[self._entrance_point.y][self._entrance_point.x]

    @property
    def exit(self) -> Room:
        return self.rooms[self._exit_point.y][self._exit_point.x]


@dataclass
class Path:
    path: List[Room]

    def __init__(self) -> None:
        self.path = []

    def visit(self, room: Room) -> Path:
        assert not self.is_visited(room)
        new_path = Path()
        new_path.path = self.path.copy()
        new_path.path.append(room)
        return new_path

    def is_visited(self, room: Room) -> bool:
        return room in self.path

    @property
    def current_room(self) -> Room | None:
        """현재 있는 방을 반환합니다."""
        if not self.path:
            return None
        else:
            return self.path[-1]

    @property
    def visitable_rooms(self) -> Generator[Room]:
        """현재 있는 방에서 다음으로 이동 할 수 있는 방들을 반환합니다."""
        assert self.path

        def _inner_generator():
            room = self.current_room
            for next_room in filter(lambda r: r is not None,
                                    (room.left, room.right, room.up, room.down)):
                if not self.is_visited(next_room):
                    yield next_room
        return _inner_generator()


    def print_map(self) -> None:
        width = self.current_room.laboratory.width
        height = self.current_room.laboratory.height
        table = [[None]*width for y in range(height)]
        for index, room in enumerate(self.path):
            table[room.y][room.x] = index+1
        for row in table:
            for col in row:
                if col is None:
                    col = -1
                print(f'[{col:2d}]', end='')
            print()


def solution():
    laboratory = Laboratory(width=4,
                            height=4,
                            entrance_point=Point(0, 0),
                            exit_point=Point(3, 3))
    # Breadth First Search 준비
    path = Path().visit(laboratory.entrance)
    queue: Deque[Path] = deque([path])
    depth = 0  # 현재 탐색중인 깊이 (이 프로그램에서는 방문한 방의 수를 의미함)
    # BFS를 응용하여 모든 방을 한 번씩 지나는 해밀턴 경로를 구함
    while queue and depth < laboratory.size:
        hamiltonian_paths: List[Path] = []  # 해밀턴 경로
        for w in range(len(queue)):
            path = queue.popleft()
            for next_room in path.visitable_rooms:
                queue.append(path.visit(next_room))
            hamiltonian_paths.append(path)
        depth += 1

    # 밀폐 경로; 해밀턴 경로 중, 출구에서 종료되는 경로만 남김
    closed_path = [*filter(lambda p: p.current_room is laboratory.exit,
                           hamiltonian_paths)]

    # 결과를 CLI에 출력
    print()
    print('해밀턴 경로')
    print()
    summary = {
        'x+y가 짝수인 경우': 0,
        'x+y가 홀수인 경우': 0
    }
    for index, path in enumerate(hamiltonian_paths):
        print(f'{index+1}번째 경우:')
        path.print_map()
        print()
        # 통계용 데이터 수집
        if (path.current_room.x + path.current_room.y) % 2 == 0:
            summary['x+y가 짝수인 경우'] += 1
        else:
            summary['x+y가 홀수인 경우'] += 1
    print('-'*64)
    print('해밀턴 경로의 수:', len(hamiltonian_paths))
    print()
    print('x+y가 짝수인 경우:', summary['x+y가 짝수인 경우'])
    print('x+y가 홀수인 경우:', summary['x+y가 홀수인 경우'])
    print()
    print('='*64)
    print()
    print('밀폐 경로')
    print()
    for index, path in enumerate(closed_path):
        print(f'{index+1}번째 경우:')
        path.print_map()
        print()
    print('-'*64)
    print('밀폐 경로의 수:', len(closed_path))


if __name__ == "__main__":
    solution()

```

</details>

<details>
<summary>실행 결과</summary>

```

해밀턴 경로

1번째 경우:
[ 1][ 2][ 3][ 4]
[ 8][ 7][ 6][ 5]
[ 9][10][11][12]
[16][15][14][13]

2번째 경우:
[ 1][ 2][ 3][ 4]
[ 8][ 7][ 6][ 5]
[ 9][16][15][14]
[10][11][12][13]

3번째 경우:
[ 1][ 2][ 3][ 4]
[ 8][ 7][ 6][ 5]
[ 9][12][13][14]
[10][11][16][15]

4번째 경우:
[ 1][ 2][ 3][ 4]
[ 8][ 7][ 6][ 5]
[ 9][12][13][16]
[10][11][14][15]

5번째 경우:
[ 1][ 2][ 3][ 4]
[16][ 7][ 6][ 5]
[15][ 8][ 9][10]
[14][13][12][11]

6번째 경우:
[ 1][ 2][ 3][ 4]
[10][ 9][ 6][ 5]
[11][ 8][ 7][16]
[12][13][14][15]

7번째 경우:
[ 1][ 2][ 3][ 4]
[16][15][ 6][ 5]
[13][14][ 7][ 8]
[12][11][10][ 9]

8번째 경우:
[ 1][ 2][ 3][ 4]
[14][15][ 6][ 5]
[13][16][ 7][ 8]
[12][11][10][ 9]

9번째 경우:
[ 1][ 2][ 3][ 4]
[14][13][ 6][ 5]
[15][12][ 7][ 8]
[16][11][10][ 9]

10번째 경우:
[ 1][ 2][ 3][ 4]
[16][15][14][ 5]
[11][12][13][ 6]
[10][ 9][ 8][ 7]

11번째 경우:
[ 1][ 2][ 3][ 4]
[12][13][14][ 5]
[11][16][15][ 6]
[10][ 9][ 8][ 7]

12번째 경우:
[ 1][ 2][ 3][ 4]
[12][13][16][ 5]
[11][14][15][ 6]
[10][ 9][ 8][ 7]

13번째 경우:
[ 1][ 2][ 3][ 4]
[14][13][12][ 5]
[15][10][11][ 6]
[16][ 9][ 8][ 7]

14번째 경우:
[ 1][ 2][ 3][ 4]
[14][15][16][ 5]
[13][10][ 9][ 6]
[12][11][ 8][ 7]

15번째 경우:
[ 1][ 2][ 3][ 4]
[12][11][10][ 5]
[13][14][ 9][ 6]
[16][15][ 8][ 7]

16번째 경우:
[ 1][ 2][ 3][ 4]
[12][11][10][ 5]
[13][16][ 9][ 6]
[14][15][ 8][ 7]

17번째 경우:
[ 1][ 2][ 3][ 4]
[16][11][10][ 5]
[15][12][ 9][ 6]
[14][13][ 8][ 7]

18번째 경우:
[ 1][ 2][ 3][16]
[ 6][ 5][ 4][15]
[ 7][10][11][14]
[ 8][ 9][12][13]

19번째 경우:
[ 1][ 2][ 3][16]
[ 8][ 7][ 4][15]
[ 9][ 6][ 5][14]
[10][11][12][13]

20번째 경우:
[ 1][ 2][ 9][10]
[ 4][ 3][ 8][11]
[ 5][ 6][ 7][12]
[16][15][14][13]

21번째 경우:
[ 1][ 2][13][12]
[ 4][ 3][14][11]
[ 5][16][15][10]
[ 6][ 7][ 8][ 9]

22번째 경우:
[ 1][ 2][11][12]
[ 4][ 3][10][13]
[ 5][ 8][ 9][14]
[ 6][ 7][16][15]

23번째 경우:
[ 1][ 2][15][16]
[ 4][ 3][14][13]
[ 5][ 8][ 9][12]
[ 6][ 7][10][11]

24번째 경우:
[ 1][ 2][15][14]
[ 4][ 3][16][13]
[ 5][ 8][ 9][12]
[ 6][ 7][10][11]

25번째 경우:
[ 1][ 2][ 5][ 6]
[16][ 3][ 4][ 7]
[15][12][11][ 8]
[14][13][10][ 9]

26번째 경우:
[ 1][ 2][ 7][ 8]
[16][ 3][ 6][ 9]
[15][ 4][ 5][10]
[14][13][12][11]

27번째 경우:
[ 1][16][15][14]
[ 2][ 3][ 4][13]
[ 7][ 6][ 5][12]
[ 8][ 9][10][11]

28번째 경우:
[ 1][ 4][ 5][ 6]
[ 2][ 3][ 8][ 7]
[11][10][ 9][16]
[12][13][14][15]

29번째 경우:
[ 1][ 4][ 5][ 6]
[ 2][ 3][ 8][ 7]
[15][16][ 9][10]
[14][13][12][11]

30번째 경우:
[ 1][ 4][ 5][ 6]
[ 2][ 3][ 8][ 7]
[15][14][ 9][10]
[16][13][12][11]

31번째 경우:
[ 1][ 4][ 5][ 6]
[ 2][ 3][16][ 7]
[13][14][15][ 8]
[12][11][10][ 9]

32번째 경우:
[ 1][ 4][ 5][16]
[ 2][ 3][ 6][15]
[ 9][ 8][ 7][14]
[10][11][12][13]

33번째 경우:
[ 1][16][15][14]
[ 2][ 3][12][13]
[ 5][ 4][11][10]
[ 6][ 7][ 8][ 9]

34번째 경우:
[ 1][ 8][ 9][10]
[ 2][ 7][ 6][11]
[ 3][ 4][ 5][12]
[16][15][14][13]

35번째 경우:
[ 1][ 6][ 7][ 8]
[ 2][ 5][10][ 9]
[ 3][ 4][11][12]
[16][15][14][13]

36번째 경우:
[ 1][16][15][14]
[ 2][11][12][13]
[ 3][10][ 9][ 8]
[ 4][ 5][ 6][ 7]

37번째 경우:
[ 1][12][13][14]
[ 2][11][16][15]
[ 3][10][ 9][ 8]
[ 4][ 5][ 6][ 7]

38번째 경우:
[ 1][12][13][16]
[ 2][11][14][15]
[ 3][10][ 9][ 8]
[ 4][ 5][ 6][ 7]

39번째 경우:
[ 1][14][13][12]
[ 2][15][10][11]
[ 3][16][ 9][ 8]
[ 4][ 5][ 6][ 7]

40번째 경우:
[ 1][14][15][16]
[ 2][13][10][ 9]
[ 3][12][11][ 8]
[ 4][ 5][ 6][ 7]

41번째 경우:
[ 1][12][11][10]
[ 2][13][14][ 9]
[ 3][16][15][ 8]
[ 4][ 5][ 6][ 7]

42번째 경우:
[ 1][12][11][10]
[ 2][13][16][ 9]
[ 3][14][15][ 8]
[ 4][ 5][ 6][ 7]

43번째 경우:
[ 1][16][11][10]
[ 2][15][12][ 9]
[ 3][14][13][ 8]
[ 4][ 5][ 6][ 7]

44번째 경우:
[ 1][10][11][12]
[ 2][ 9][ 8][13]
[ 3][ 6][ 7][14]
[ 4][ 5][16][15]

45번째 경우:
[ 1][14][15][16]
[ 2][13][12][11]
[ 3][ 6][ 7][10]
[ 4][ 5][ 8][ 9]

46번째 경우:
[ 1][14][13][12]
[ 2][15][16][11]
[ 3][ 6][ 7][10]
[ 4][ 5][ 8][ 9]

47번째 경우:
[ 1][16][13][12]
[ 2][15][14][11]
[ 3][ 6][ 7][10]
[ 4][ 5][ 8][ 9]

48번째 경우:
[ 1][16][15][14]
[ 2][ 7][ 8][13]
[ 3][ 6][ 9][12]
[ 4][ 5][10][11]

49번째 경우:
[ 1][ 8][ 9][10]
[ 2][ 7][12][11]
[ 3][ 6][13][14]
[ 4][ 5][16][15]

50번째 경우:
[ 1][ 8][ 9][10]
[ 2][ 7][12][11]
[ 3][ 6][13][16]
[ 4][ 5][14][15]

51번째 경우:
[ 1][ 8][ 9][10]
[ 2][ 7][16][11]
[ 3][ 6][15][12]
[ 4][ 5][14][13]

52번째 경우:
[ 1][ 8][ 9][16]
[ 2][ 7][10][15]
[ 3][ 6][11][14]
[ 4][ 5][12][13]

----------------------------------------------------------------
해밀턴 경로의 수: 52

x+y가 짝수인 경우: 0
x+y가 홀수인 경우: 52

================================================================

밀폐 경로

----------------------------------------------------------------
밀폐 경로의 수: 0
```

</details>
