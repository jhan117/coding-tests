/**
 * [23.02.01 - Baekjoon] 1463 1로 만들기
 * @param {number} N 1 <= N <= 10^6 (정수)
 * @returns {number} 연산을 하는 횟수의 최솟값
 */
function makeOne(N) {
  d = Array(N + 1).fill(0);
  d[2] = d[3] = 1;

  for (let i = 4; i <= N; i++) {
    d[i] = d[i - 1] + 1;
    if (i % 3 === 0) {
      d[i] = Math.min(d[i / 3] + 1, d[i]);
    }
    if (i % 2 === 0) {
      d[i] = Math.min(d[i / 2] + 1, d[i]);
    }
  }
  return d[N];
}

// 인접 행렬
const graph = Array.from({ length: n + 1 }, () => []);
/**
 * [23.02.03 - Baekjoon] 1260 DFS와 BFS
 * @param {boolean} isBFS true이면 BFS, false이면 DFS
 * @returns {string} 방문한 순서
 */
function DFSandBFS(isBFS = false) {
  if (isBFS) graph.map((nodes) => nodes.sort((a, b) => a - b));
  else graph.map((nodes) => nodes.sort((a, b) => b - a));
  const visited = Array(n + 1).fill(false);
  const data = [v];
  const answer = [];

  while (data.length) {
    if (isBFS) var node = data.shift();
    else var node = data.pop();
    if (!visited[node]) {
      visited[node] = true;
      answer.push(node);
      data.push(...graph[node]);
    }
  }
  return answer.join(" ");
}

/**
 * [23.02.05 - Baekjoon] 2178 미로 탐색
 * @param {number} N Y 끝 좌표
 * @param {number} M X 끝 좌표
 * @param {[]} graph 인접 행렬
 * @returns {number} 지나야 하는 최소의 칸 수
 */
function mazeSearch(N, M, graph) {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  const visited = Array.from({ length: N }, () => Array(M).fill(0));
  const queue = [[0, 0]]; // x, y

  visited[0][0] = 1;

  while (queue.length) {
    [x, y] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const nextY = y + dy[i];
      const nextX = x + dx[i];

      if (nextX < 0 || M <= nextX || nextY < 0 || N <= nextY) continue;
      if (graph[nextY][nextX] && !visited[nextY][nextX]) {
        visited[nextY][nextX] = visited[y][x] + 1;
        queue.push([nextX, nextY]);
      }
    }
  }
  return visited[N - 1][M - 1];
}

/**
 * [23.02.06 - Baekjoon] 1149 RGB거리
 * @param {number} N 집 개수
 * @param {[]} costs 색깔별 비용 배열
 * @returns {number} 모든 집을 칠하는 비용의 최솟값
 */
function RGB(N, costs) {
  const dp = Array.from({ length: N }, () => []);
  const idxs = [
    [1, 2],
    [0, 2],
    [0, 1],
  ];

  dp[0] = costs[0];

  for (let i = 1; i < N; i++) {
    const arr = dp[i - 1];
    for (let j = 0; j < 3; j++) {
      const [f, s] = idxs[j];
      dp[i][j] = Math.min(arr[f], arr[s]) + costs[i][j];
    }
  }
  return Math.min(...dp[N - 1]);
}

/**
 * [23.02.07 - Baekjoon] 1074 Z
 * @param {number} n 2^n x 2^n, 2차원 배열 크기
 * @param {number} r 행
 * @param {number} c 열
 * @returns {number} r행 c열을 방문한 순서
 */
function Z(n, r, c) {
  if (n === 0) return 0;

  const size = 2 ** ((n - 1) * 2);
  const half = 2 ** n / 2;

  if (r < half && c < half) {
    return Z(n - 1, r, c);
  } else if (r < half && c >= half) {
    return size + Z(n - 1, r, c - half);
  } else if (r >= half && c < half) {
    return size * 2 + Z(n - 1, r - half, c);
  } else {
    return size * 3 + Z(n - 1, r - half, c - half);
  }
}

/**
 * [23.02.08 - Baekjoon] 2667 단지번호붙이기
 * @param {number} N 지도의 크기
 * @param {[]} graph 2차원 배열의 정사각형 지도
 * @returns {string} 총 단지수 + 각 단지내의 집의 수(오름차순)
 */
function complexNumbering(N, graph) {
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];

  let complex = 0;
  const homeCnt = [];

  for (let y = 0; y < N; y++) {
    for (let x = 0; x < N; x++) {
      if (graph[y][x]) {
        const stack = [[x, y]];

        let cnt = 0;
        while (stack.length) {
          const [cx, cy] = stack.pop();

          if (graph[cy][cx]) {
            graph[cy][cx] = 0;
            cnt++;
            for (let i = 0; i < 4; i++) {
              const [nx, ny] = [cx + dx[i], cy + dy[i]];
              if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
              if (graph[ny][nx]) {
                stack.push([nx, ny]);
              }
            }
          }
        }
        complex++;
        homeCnt.push(cnt);
      }
    }
  }
  return complex + "\n" + homeCnt.sort((a, b) => a - b).join("\n");
}

/**
 * [23.02.09 - Baekjoon] 1991 트리 순회
 * @param {{}} tree 트리
 * @returns {string} 전회, 중위, 후위 순회 결과
 */
function tourTree(tree) {
  let answer = "";

  preorder("A");
  answer += "\n";
  inorder("A");
  answer += "\n";
  postorder("A");

  return answer;

  function preorder(node) {
    if (node === ".") return;
    const [l, r] = tree[node];
    answer += node;
    preorder(l);
    preorder(r);
  }

  function inorder(node) {
    if (node === ".") return;
    const [l, r] = tree[node];
    inorder(l);
    answer += node;
    inorder(r);
  }

  function postorder(node) {
    if (node === ".") return;
    const [l, r] = tree[node];
    postorder(l);
    postorder(r);
    answer += node;
  }
}
