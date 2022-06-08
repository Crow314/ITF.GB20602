import math
from numbers import Number
from copy import deepcopy

INF = float('inf')


class MaxFlow:
    def __init__(self, V: int):
        self.V = V
        self.EL = []
        self.AL = [list() for _ in range(self.V)]
        self.d = []
        self.last = []
        self.p = []
        self.has_been_run = False

    def BFS(self, s: int, t: int) -> bool:
        self.d = [-1] * self.V
        self.d[s] = 0
        self.p = [[-1, -1] for _ in range(self.V)]
        q = [s]
        while len(q) != 0:
            u = q[0]
            q.pop(0)
            if u == t:
                break
            for idx in self.AL[u]:
                v, cap, flow = self.EL[idx]
                if cap - flow > 0 and self.d[v] == -1:
                    self.d[v] = self.d[u]+1
                    q.append(v)
                    self.p[v] = [u, idx]
        return self.d[t] != -1

    def send_one_flow(self, s: int, t: int, f: Number = INF) -> Number:
        if s == t:
            return f
        u, idx = self.p[t]
        _, cap, flow = self.EL[idx]
        pushed = self.send_one_flow(s, u, min(f, cap-flow))
        flow += pushed
        self.EL[idx][2] = flow
        self.EL[idx ^ 1][2] -= pushed
        return pushed

    def DFS(self, u: int, t: int, f: Number = INF) -> Number:
        if u == t or f == 0:
            return f
        for i in range(self.last[u], len(self.AL[u])):
            self.last[u] = i
            v, cap, flow = self.EL[self.AL[u][i]]
            if self.d[v] != self.d[u]+1:
                continue
            pushed = self.DFS(v, t, min(f, cap - flow))
            if pushed != 0:
                flow += pushed
                self.EL[self.AL[u][i]][2] = flow
                self.EL[self.AL[u][i] ^ 1][2] -= pushed
                return pushed
        return 0

    def add_edge(self, u: int, v: int, capacity: Number,
                 directed: bool = True) -> None:
        if u == v:
            return
        self.EL.append([v, capacity, 0])
        self.AL[u].append(len(self.EL)-1)
        self.EL.append([u, 0 if directed else capacity, 0])
        self.AL[v].append(len(self.EL)-1)

    def assert_has_not_already_been_run(self):
        if self.has_been_run:
            msg = ('Rerunning a max flow algorithm on the same graph will '
                   + 'result in incorrect behaviour. Please use .copy() '
                   + 'before you run any max flow algorithm if you need to '
                   + 'run multiple iterations')
            raise Exception(msg)

        self.has_been_run = True

    def dinic(self, s: int, t: int) -> Number:
        self.assert_has_not_already_been_run()

        mf = 0
        while self.BFS(s, t):
            self.last = [0] * self.V
            f = self.DFS(s, t)
            while f != 0:
                mf += f
                f = self.DFS(s, t)
        return mf

    def copy(self) -> 'MaxFlow':
        return deepcopy(self)

    def __repr__(self) -> str:
        el = self.EL[:10] + ['...'] if len(self.EL) > 10 else self.EL
        al = self.AL[:10] + ['...'] if len(self.AL) > 10 else self.AL
        el = ', '.join(map(str, el))
        al = ', '.join(map(str, al))
        return f'MaxFlow(V={self.V}, EL=[{el}], AL=[{al}])'


def adj_list(mf: MaxFlow, field: list, row: int, column: int):
    FREE_PATH = 10 ** 6
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # <v^>

    for i in range(row):
        for j in range(column):
            in_idx = (i * column + j) * 2  # in
            out_idx = (i * column + j) * 2 + 1  # out
            mf.add_edge(in_idx, out_idx, field[i][j])

            for direction in directions:
                x = j + direction[0]
                y = i + direction[1]

                next_idx = (y * column + x) * 2  # in

                if (x < 0) or (x >= column) or (y < 0) or (y >= row):
                    continue

                mf.add_edge(out_idx, next_idx, FREE_PATH)


def main():
    R, C = map(int, input().split())

    SPACE = 10 ** 6
    SPACE_ROW = [SPACE for _ in range(C+2)]

    field = [SPACE_ROW.copy()]
    for _ in range(R):
        tmp_row = [SPACE]
        tmp_row += list(map(int, input().split()))
        tmp_row.append(SPACE)

        field.append(tmp_row)
    field.append(SPACE_ROW.copy())

    r, c = map(int, input().split())
    start = 0
    goal = (C+2) * (r+1) + c + 1
    goal_idx = goal * 2 + 1

    field_count = C * (R+1) + R * (C+1) + 1
    vertex_count = field_count * 2

    mf = MaxFlow(vertex_count * 2)
    adj_list(mf, field, R+2, C+2)
    print(mf.dinic(start, goal_idx))


if __name__ == '__main__':
    main()
