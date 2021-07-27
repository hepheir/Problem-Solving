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
    print('헤밀턴 경로')
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
