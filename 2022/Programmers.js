function solution_142086(s) {
  // 가장 가까운 같은 글자
  let seen = {};
  let answer = [];

  s.split("").forEach((item, idx) => {
    if (item in seen) {
      answer.push(idx - seen[item]);
    } else {
      answer.push(-1);
    }
    seen[item] = idx;
  });

  return answer;
}

function heapPush(heap, item) {
  if (heap.length === 0) {
    heap.push(item);
  } else {
    // 최대 힙
    for (let i = 0; i < heap.length; i++) {
      if (heap[i] < item) {
        heap.splice(i, 0, item);
        break;
      }
      heap.push(item);
    }
  }
}

function isDefense(mid, n, k, enemy) {
  const maxHeap = [];

  enemy.slice(0, mid + 1).forEach((e) => heapPush(maxHeap, e));

  while (maxHeap) {
    if (n >= maxHeap[-1]) {
      n -= maxHeap.pop();
      continue;
    }
    return k >= maxHeap.length;
  }

  return true;
}

function search(n, k, enemy) {
  let left = 0,
    right = enemy.length;

  while (left < right) {
    const mid = Math.ceil((left + right) / 2);

    if (isDefense(mid, n, k, enemy)) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}

function solution_142085(n, k, enemy) {
  // 디펜스 게임

  return search(n, k, enemy);
}

function solution_140107(k, d) {
  // 점 찍기

  let a = 0,
    b = 0;
  let answer = 0;

  while (true) {
    const x = a * k;
    if (x > d) return answer; // x 종료

    while (true) {
      const y = b * k;
      if (y > d) break; // y 종료

      const diagonal = Math.sqrt(x ** 2 + y ** 2);
      // console.log(x, y, diagonal);
      if (diagonal <= d) {
        answer++;
      } else break;
      b++;
    }
    b = 0;
    a++;
  }
}
