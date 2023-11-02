# BFS

(bfs)=
## Breadth First Search

> 너비 우선 탐색
> 정점들과 같은 레벨에 있는 노드들(형제 노드)을 먼저 탐색하는 방식

보통 `queue`를 이용하여 구현한다.

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
