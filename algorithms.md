# 목차

## 최단 경로

가장 짧은 경로를 찾는 알고리즘이다.

- [다익스트라 최단 경로 알고리즘](#다익스트라dijkstra-데이크스트라-최단-경로-알고리즘)
- [플로이드 워셜 알고리즘](#플로이드-워셜floyd-warshall-알고리즘)
- 벨만 포드 알고리즘

### 다익스트라(Dijkstra, 데이크스트라) 최단 경로 알고리즘

[소스 코드 확인하기](/algorithms.py#L8-L42)

- 한 노드에서 출발하여 다른 특정 노드까지의 최단 경로를 구해주는 알고리즘
- 음의 간선이 없을 때 정상적으로 동작함
- 항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다는 특징
- 그리디 알고리즘으로 분류됨
- 우선순위 큐를 사용할시 시간 복잡도 : O(ElogV)

1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산해 최단 거리 테이블 갱신
5. 3-4번 반복

### 플로이드 워셜(Floyd Warshall) 알고리즘

[소스 코드 확인하기](/algorithms.py#L45-L78)

- 모든 노드에서 출발하여 다른 모든 노드까지의 최단 경로를 구해주는 알고리즘
- 다이나믹 프로그래밍으로 분류됨
- 시간 복잡도 : O($N^3$)

점화식 : $D_{ab} = min(D_{ab},\ D_{ak} + D_{kb})$  
이 때, a -> b, k는 거쳐가는 노드 번호이다. 즉, ak + kb = a -> k -> b  
예를 들어, 4개의 노드가 존재할 때 1번 노드를 거쳐가는 경우의 수는 $_3P_2$ = 6가지이다.  
이 6가지 경우만 하나씩 확인하며 값을 계산하여 갱신한다.