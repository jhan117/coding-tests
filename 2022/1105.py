from collections import deque
from unittest import TestCase, main


class Tests(TestCase):
    def test_도시(self):
        result1 = Submit().특정_거리의_도시_찾기(
            4, 2, 1, [[1, 2], [1, 3], [2, 3], [2, 4]])
        self.assertEqual(result1, '4')


class Submit:
    """내가 작성한 코드"""

    def 특정_거리의_도시_찾기(self, n: int, k: int, x: int, graph: list[list[int]]):
        ans = []
        visited = [-1] * (n + 1)

        queue = deque([x])
        visited[x] = 0

        while queue:
            v = queue.popleft()
            for l in graph:
                if l[0] > v:
                    break
                i = l[1]
                if visited[i] == -1:
                    queue.append(i)
                    visited[i] = 0
                    visited[i] = visited[v] + 1

                    if visited[i] == k:
                        ans.append(str(i))

        if ans:
            ans.sort()
            return ' '.join(ans)
        return -1


if __name__ == '__main__':
    main()
