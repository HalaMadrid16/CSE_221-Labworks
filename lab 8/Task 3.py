import sys
import heapq
from collections import defaultdict

input = sys.stdin.read
data = input().split()
idx = 0

# Input reading
N, M = int(data[idx]), int(data[idx + 1])
idx += 2

edges = []
for _ in range(M):
    u, v, w = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
    edges.append((w, u, v))
    idx += 3

# Kruskal's MST
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

edges.sort()  # Sort edges by weight
parent = list(range(N + 1))
rank = [0] * (N + 1)

mst = []  # Store edges in the MST
mst_weight = 0
mst_edges = set()  # To quickly identify MST edges
tree = defaultdict(list)

for w, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        mst.append((u, v, w))
        mst_weight += w
        mst_edges.add((u, v))
        mst_edges.add((v, u))
        tree[u].append((v, w))
        tree[v].append((u, w))

# Check if MST is valid (i.e., fully connected)
if len(mst) != N - 1:
    print(-1)
    sys.exit()

# Binary Lifting Preprocessing
LOG = 17  # Sufficient for N ≤ 10^3
depth = [-1] * (N + 1)
parent = [[-1] * LOG for _ in range(N + 1)]
max_edge = [[0] * LOG for _ in range(N + 1)]

def dfs(node, par, weight):
    depth[node] = depth[par] + 1
    parent[node][0] = par
    max_edge[node][0] = weight
    for v, w in tree[node]:
        if v != par:
            dfs(v, node, w)

# Initialize DFS and preprocess
depth[0] = -1
dfs(1, 0, 0)

for k in range(1, LOG):
    for i in range(1, N + 1):
        if parent[i][k - 1] != -1:
            parent[i][k] = parent[parent[i][k - 1]][k - 1]
            max_edge[i][k] = max(max_edge[i][k - 1], max_edge[parent[i][k - 1]][k - 1])

# Max Edge Query on Path using Binary Lifting
def get_max_edge(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    res = 0
    for k in reversed(range(LOG)):
        if depth[u] - (1 << k) >= depth[v]:
            res = max(res, max_edge[u][k])
            u = parent[u][k]
    if u == v:
        return res
    for k in reversed(range(LOG)):
        if parent[u][k] != parent[v][k]:
            res = max(res, max_edge[u][k], max_edge[v][k])
            u = parent[u][k]
            v = parent[v][k]
    return max(res, max_edge[u][0], max_edge[v][0])

# Try adding non-MST edges
second_best = float('inf')
for w, u, v in edges:
    if (u, v) not in mst_edges and (v, u) not in mst_edges:
        max_in_cycle = get_max_edge(u, v)
        new_weight = mst_weight - max_in_cycle + w
        if new_weight > mst_weight:
            second_best = min(second_best, new_weight)

# Output the result
print(second_best if second_best != float('inf') else -1)
