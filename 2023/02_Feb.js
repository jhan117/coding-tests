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

/**
 * [23.02.10 - Baekjoon] 12865 평범한 배낭
 * @param {number} N 물품 수
 * @param {number} K 버틸 수 있는 무게
 * @param {number[]} items 물건의 무게와 물건의 가치 배열
 * @returns {number} 가치 합의 최댓값
 */
function backpack(N, K, items) {
  const dp = Array.from({ length: N + 1 }, () => Array(K + 1).fill(0));

  for (let r = 1; r <= N; r++) {
    for (let c = 1; c <= K; c++) {
      const [w, v] = items[r - 1];
      if (w > c && dp[r - 1][c] === 0) continue;
      const leftValue = dp[r - 1][c - w] + v || 0;
      dp[r][c] = Math.max(dp[r - 1][c], leftValue);
    }
  }
  return dp[N][K];
}

/**
 * [23.02.11 - Baekjoon] 9663 N-Queen
 * @param {number} N N x N 체스판, 퀸 개수
 * @returns {number} 서로 공격할 수 없게 놓는 경우의 수
 */
function NQueen(N) {
  const row = Array(N).fill(0);
  return recursion(N, row, 0);
}

function recursion(N, row, n) {
  let result = 0;
  if (n === N) {
    return (result += 1);
  }

  for (let i = 0; i < N; i++) {
    row[n] = i;
    if (check(row, n)) {
      result += recursion(N, row, n + 1);
    }
  }
  return result;
}

function check(row, n) {
  for (let i = 0; i < n; i++) {
    const checkAbove = row[n] === row[i];
    const checkDiagonal = Math.abs(row[n] - row[i]) === Math.abs(n - i);
    if (checkAbove || checkDiagonal) return false;
  }
  return true;
}

/**
 * [23.02.14 - Baekjoon] 2206 벽 부수고 이동하기
 * @param {number} N row
 * @param {number} M column
 * @param {[]} graph N x M
 * @returns {number} 벽 최대 1개 부수고 간 최단 거리
 */
function breakWall(N, M, graph) {
  // visited[row][column][broken]
  const visited = Array.from({ length: N }, () =>
    Array.from({ length: M }, () => Array(2).fill(0))
  );

  const [dr, dc] = [
    [-1, 1, 0, 0],
    [0, 0, -1, 1],
  ];

  const queue = new Queue();
  queue.enqueue([0, 0, 0]);
  visited[0][0][0] = 1;

  while (!queue.isEmpty()) {
    const [cr, cc, cb] = queue.dequeue();

    if (cr === N - 1 && cc === M - 1) {
      return visited[cr][cc][cb];
    }

    for (let i = 0; i < 4; i++) {
      const [nr, nc] = [cr + dr[i], cc + dc[i]];

      if (nr < 0 || nc < 0 || nr >= N || nc >= M) continue;
      if (visited[nr][nc][cb]) continue;

      // next is 1 and broken is 0
      if (graph[nr][nc] && !cb) {
        visited[nr][nc][1] = visited[cr][cc][cb] + 1;
        queue.enqueue([nr, nc, 1]);
      }
      // next is 0
      if (!graph[nr][nc]) {
        visited[nr][nc][cb] = visited[cr][cc][cb] + 1;
        queue.enqueue([nr, nc, cb]);
      }
    }
  }
  return -1;
}

/**
 * [23.02.17 - Baekjoon] 12100 2048 (Easy)
 * @param {number} N 보드판 크기
 * @param {[]} board 보드판
 * @returns {number} 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록의 숫자
 */
function play2048(N, board) {
  const direction = ["top", "down", "left", "right"];

  return play2048Recursion(N, direction, board, 5, []);
}

function play2048Recursion(N, direction, board, cnt, answer) {
  if (cnt === 0) {
    const curMax = Math.max(...board.flat());
    return answer.push(curMax);
  }

  for (let i = 0; i < 4; i++) {
    const movedBoard = moving(N, direction[i], board);
    play2048Recursion(N, direction, movedBoard, cnt - 1, answer);
  }
  return Math.max(...answer);
}

function moving(N, direction, board) {
  const copiedBoard = board.map((v) => v.slice());
  const isTopDown = direction === "top" || direction === "down" ? true : false;

  if (isTopDown) {
    // 세로 배열 생성
    for (let c = 0; c < N; c++) {
      const rows = [];
      for (let r = 0; r < N; r++) {
        if (copiedBoard[r][c]) {
          rows.push(copiedBoard[r][c]);
        }
      }
      if (direction === "down") rows.reverse();

      for (let r = 0; r < rows.length; r++) {
        const nextRow = r + 1;

        if (nextRow < 0 || nextRow >= rows.length) break;
        const currentNum = rows[r];
        const nextNum = rows[nextRow];
        if (currentNum === nextNum) {
          rows[r] = currentNum * 2;
          rows.splice(nextRow, 1);
        }
      }

      if (rows.length) {
        for (let r = 0; r < N; r++) {
          const row = direction === "top" ? r : N - 1 - r;

          if (rows[r]) {
            copiedBoard[row][c] = rows[r];
          } else {
            copiedBoard[row][c] = 0;
          }
        }
      }
    }
  } else {
    // 가로 배열 생성
    for (let r = 0; r < N; r++) {
      const cols = copiedBoard[r].filter((v) => v);
      if (direction === "right") cols.reverse();

      for (let c = 0; c < cols.length; c++) {
        const nextCol = c + 1;

        if (nextCol < 0 || nextCol >= cols.length) break;
        const currentNum = cols[c];
        const nextNum = cols[nextCol];
        if (currentNum === nextNum) {
          cols[c] = currentNum * 2;
          cols.splice(nextCol, 1);
        }
      }

      if (cols.length) {
        for (let c = 0; c < N; c++) {
          const col = direction === "left" ? c : N - 1 - c;

          if (cols[c]) {
            copiedBoard[r][col] = cols[c];
          } else {
            copiedBoard[r][col] = 0;
          }
        }
      }
    }
  }
  return copiedBoard;
}

// [23.02.20 - Baekjoon] 2098 외판원 순회
class TSPClass {
  constructor(input) {
    const inputs = input.split("\n");

    this.N = Number(inputs.shift());
    this.costs = inputs.map((v) => v.split(" ").map(Number));

    this.dp = Array.from({ length: 1 << this.N }, () => []);
  }

  main() {
    let answer;
    answer = this.DFS(0, 0);

    // 경우의 수가 없는 경우 -1 출력
    if (answer === Infinity) return -1;
    return answer;
  }

  // visited : 이미 방문한 도시 체크
  // now : 이번에 지날 도시 번호
  DFS(visited, now) {
    // now 도시 번호 추가
    visited |= 1 << now;

    // 모든 도시를 지난 경우
    if (visited === (1 << this.N) - 1) {
      // now → 0으로 가는 경우 있으면 반환
      if (this.costs[now][0]) return this.costs[now][0];
      return Infinity;
    }

    // dp 배열에 저장되어 있는 경우 그 값 반환
    if (this.dp[visited][now] > 0) return this.dp[visited][now];

    // 없는 경우 무한 넣기
    this.dp[visited][now] = Infinity;
    // 모든 도시 방문
    for (let i = 0; i < this.N; i++) {
      // 방문하려는 i와 now 번호가 같지 않아야 하고
      // 방문되어 있지 않아야 하며
      // 갈 수 있는 경로가 있어야 한다.
      if (i !== now && !(visited & (1 << i)) && this.costs[now][i] > 0) {
        // 최소 비용 갱신
        // 방문 현황과 현재 도시가 같을 때,
        // 방문하지 않은 도시들을 모두 거쳐서 시작점으로 돌아가는 데 드는 최소 비용을 말한다.
        this.dp[visited][now] = Math.min(
          this.dp[visited][now],
          this.DFS(visited, i) + this.costs[now][i]
        );
      }
    }
    return this.dp[visited][now];
  }
}

// [23.02.22 - Baekjoon] 13460 구슬 탈출 2
class BeadEscape2 {
  constructor(input) {
    const inputs = input.split("\n");

    [this.N, this.M] = inputs.shift().split(" ").map(Number);
    this.board = inputs.map((v) => v.split(""));

    this.dr = [-1, 1, 0, 0];
    this.dc = [0, 0, -1, 1];

    // visited[Red Row][Red Col][Blue Row][Blue Col]
    this.visited = Array.from({ length: this.N }, () =>
      Array.from({ length: this.M }, () =>
        Array.from({ length: this.N }, () => Array(this.M).fill(false))
      )
    );

    let rRow, rCol, bRow, bCol;

    this.board.forEach((v, i) => {
      const red = v.findIndex((v) => v === "R");
      const blue = v.findIndex((v) => v === "B");
      if (red !== -1) {
        rRow = i;
        rCol = red;
      }
      if (blue !== -1) {
        bRow = i;
        bCol = blue;
      }
    });
    this.queue = [[rRow, rCol, bRow, bCol, 1]];
    this.visited[rRow][rCol][bRow][bCol] = true;
  }

  main() {
    while (this.queue.length) {
      const [rRow, rCol, bRow, bCol, depth] = this.queue.shift();

      if (depth > 10) return -1;

      for (let i = 0; i < 4; i++) {
        let [nrRow, nrCol, rCnt] = this.move(rRow, rCol, i);
        let [nbRow, nbCol, bCnt] = this.move(bRow, bCol, i);

        if (this.board[nbRow][nbCol] === "O") continue;
        if (this.board[nrRow][nrCol] === "O") return depth;
        if (nrCol === nbCol && nrRow === nbRow) {
          if (rCnt > bCnt) {
            nrRow -= this.dr[i];
            nrCol -= this.dc[i];
          } else {
            nbRow -= this.dr[i];
            nbCol -= this.dc[i];
          }
        }
        if (!this.visited[nrRow][nrCol][nbRow][nbCol]) {
          this.visited[nrRow][nrCol][nbRow][nbCol] = true;
          this.queue.push([nrRow, nrCol, nbRow, nbCol, depth + 1]);
        }
      }
    }
    return -1;
  }

  move(r, c, dIdx) {
    const [mr, mc] = [this.dr[dIdx], this.dc[dIdx]];
    let cnt = 0;
    while (this.board[r + mr][c + mc] !== "#" && this.board[r][c] !== "O") {
      r += mr;
      c += mc;
      cnt += 1;
    }
    return [r, c, cnt];
  }
}
