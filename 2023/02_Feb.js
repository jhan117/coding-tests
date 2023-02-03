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

console.log(makeOne(Number(N)));

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

console.log(DFSandBFS());
console.log(DFSandBFS(true));
