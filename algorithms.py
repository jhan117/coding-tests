import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


class DijkstraAlgorithm:
    def __init__(self) -> None:
        # 입력
        N, V = map(int, input().split())
        start = int(input())
        self.graph = [[] for _ in range(N + 1)]
        self.distance = [INF] * (N + 1)
        for _ in range(V):
            # a -> b, 비용 c
            a, b, c = map(int, input().split())
            self.graph[a].append((b, c))

        # 시작
        self.dijkstra(start)

        # 출력
        for i in range(1, N + 1):
            if self.distance[i] == INF:
                print('Infinity')
            else:
                print(self.distance[i])

    def dijkstra(self, start) -> None:
        q = []
        heapq.heappush(q, (0, start))
        self.distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if self.distance[now] < dist:
                continue
            for i in self.graph[now]:
                cost = dist + i[1]
                if cost < self.distance[i[0]]:
                    self.distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


class FloydWarshallAlgorithm:
    def __init__(self) -> None:
        # 입력
        self.N, V = map(int, input().split())
        self.graph = [[INF] * (self.N + 1)
                      for _ in range(self.N + 1)]  # 2차원 배열
        # 자기 자신 0으로 초기화
        for a in range(1, self.N + 1):
            for b in range(1, self.N + 1):
                if a == b:
                    self.graph[a][b] = 0
        for _ in range(V):
            a, b, c = map(int, input().split())
            self.graph[a][b] = c

        # 시작
        self.floyd_warshall()

        # 출력
        for a in range(1, self.N + 1):
            for b in range(1, self.N + 1):
                if self.graph[a][b] == INF:
                    print('Infinity', end=' ')
                else:
                    print(self.graph[a][b], end=' ')
            print()

    def floyd_warshall(self) -> None:
        # 3중 for문
        for k in range(1, self.N + 1):
            for a in range(1, self.N + 1):
                for b in range(1, self.N + 1):
                    self.graph[a][b] = min(
                        self.graph[a][b], self.graph[a][k] + self.graph[k][b])


if __name__ == '__main__':
    # DijkstraAlgorithm()
    FloydWarshallAlgorithm()

"""
다익스트라 테스트 입력

6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

플로이드 워셜 테스트 입력

4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""
