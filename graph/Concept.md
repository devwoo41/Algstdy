# Graph

-G=(V,E)
V: 노드의 집합
E: 에지의 집합

# Node, Vertex

-정점

# Edge

-간선,연결선

# Degree

-한 노드에 연결된 연결선의 수

# Path

-사이클이 존재하지 않는 경로

# Cycle

-순환이 존재해서 시작 노드로 되돌아오는 경로

# 인접행렬

-그래프에서 관계를 행렬로 표현

# 인접리스트

-그래프에서 관계를 리스트로 표현

# Undirected Graph

-방향이 존재하지 않는 그래프

# Directed Graph

-방향이 존재하는 그래프

# Weighted graph

-Weighted graph의 경우, 인접행렬로 나타낼 때 인접한 엣지에 1대신 가중치 값을 넣을 수 있음.
G = (V,E)
|V| = n, |E| = m
인접 행렬의 Memory: O(n^2) – n by n 의 인접행렬로 표현하므로
인접 리스트의 Memory: O(n+m)
