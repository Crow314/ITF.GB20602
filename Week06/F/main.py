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
        """
        Returns the max flow obtained by running Dinic's algorithm.
        Modifies the graph in place.
        Arguments:
            `s`: The source vertex.
            `t`: The sink vertex.
        Returns:
            The max flow.
        """
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


def adj_list(mf: MaxFlow, rooms: list):
    n = len(rooms)

    for i in range(n):
        for j in range(i+1, n):
            cap = math.gcd(rooms[i], rooms[j])
            if cap > 1:
                mf.add_edge(i, j, cap, False)


def main():
    n = int(input())

    rooms = []
    min_vertex = 10 ** 10
    max_vertex = 0

    start = None
    goal = None

    for i in range(n):
        weight = int(input())
        rooms.append(weight)

        if weight < min_vertex:
            min_vertex = weight
            start = i

        if weight > max_vertex:
            max_vertex = weight
            goal = i

    mf = MaxFlow(n)
    adj_list(mf, rooms)
    print(mf.dinic(start, goal))


if __name__ == '__main__':
    main()
