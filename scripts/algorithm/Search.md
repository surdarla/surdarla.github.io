=(search)
# Search 탐색

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](<YOUR URL HERE>)

```{figure} ../../images/bfsvsdfs.gif
---
name : BFS vs DFS
align : center
width : 60 %
alt : bfs vs dfs image alt
---
Bfs vs Dfs
```

vs 최단경로, 최소비용 문제
: 탐색 문제는 그래프에서 경로를 찾는 것이 주된 목표다. 경로를 찾기만 하면 되는 것이고, 경로가 가중치가 있으면(비용이라던가, 거리라던가) 최단 경로 혹은 최소 비용의 경로를 찾는 문제가 된다. 이것(다익스트라, 벨만 포드)들에 대한 것은 따로 하고, 경로를 찾는 문제에 대해서만 다루겠다.

vs Greedy
: 보통 두 가지로 나뉜다. (1) 모든 경로 찾기, (2) 특정 경로 찾기. 둘 다 모든 경로를 살펴보는 것이 탐색 문제의 본질이라고 할 수 있다. Greedy랑은 다르다. Greedy는 그때그때 최선의 선택을 하는 것이고, 해당 선택은 모든 경로 중에 최선의 경로를 보장할 때 사용할 수 있다. 하지만 탐색은 모든 경우를 살펴봐야만 하는 경우에 사용한다.

When?
: 1. (가중치 없으면서) 모든 경우 구할 때 DFS
  1. 검색 대상 그래프가 너무 크면 DFS
  2. (가중치 없으면서) 최단거리를 구해야할 때는 BFS
  3. 검색 대상이 규모가 작고, 시작 지점부터 멀지 않다면 BFS

(bfs)=
## Breadth First Search

> 너비 우선 탐색\
> 정점들과 같은 레벨에 있는 노드들(형제 노드)을 먼저 탐색하는 방식
보통 [queue](queue)를 이용하여 구현한다. 이를 위해 deque를 사용한다.

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False]*9
bfs(graph, 1, visited)
```

(dfs)=
## Depth First Search
> 깊이 우선 탐색

(backtracking)=
### backtracking

```{prf:algorithm} Backtracking
:label: Backtracking

**P** : root node\
**C** : child node

void CheckNode(node P)\
{\
  node C;\
  if (promising(P)) {\
    if (there is a solution of P),\
      then writhe the solution  \
    else {\
      for (each child node C of P) {\
        checkNode(C)\
      }\
    }\
  }\  
  else\
    backtrack to parent node P\
}\
```

```{raw} html
<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="surdarla/surdarla.github.io"
   issue-term="pathname"
   theme="github-light"
   label="💬 comment"
   crossorigin="anonymous"
/>
```
