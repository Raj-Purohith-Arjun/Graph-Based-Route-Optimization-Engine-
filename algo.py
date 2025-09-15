import heapq
import math


# Dijkstra’s Algorithm

def dijkstra(graph, start, goal):
    pq = [(0, start)]  # (distance, node)
    dist = {node: math.inf for node in graph}
    dist[start] = 0
    prev = {}

    while pq:
        current_dist, u = heapq.heappop(pq)
        if u == goal:
            break
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            alt = current_dist + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))
    return reconstruct_path(prev, start, goal), dist[goal]



# Heuristic for A*

def heuristic(u, v):
    """
    Simple admissible heuristic:
    underestimate travel cost between u and v.
    Since we lack coordinates, we approximate:
    - abs difference in node IDs * 0.001
    Keeps heuristic small relative to edge weights (1–10).
    """
    return abs(u - v) * 0.001



# A* Algorithm
def astar(graph, start, goal):
    pq = [(0, start)]  # (f = g + h, node)
    g = {node: math.inf for node in graph}
    g[start] = 0
    f = {node: math.inf for node in graph}
    f[start] = heuristic(start, goal)
    prev = {}

    while pq:
        _, u = heapq.heappop(pq)
        if u == goal:
            break
        for v, weight in graph[u]:
            tentative_g = g[u] + weight
            if tentative_g < g[v]:
                g[v] = tentative_g
                f[v] = tentative_g + heuristic(v, goal)
                prev[v] = u
                heapq.heappush(pq, (f[v], v))
    return reconstruct_path(prev, start, goal), g[goal]



# Path Reconstruction

def reconstruct_path(prev, start, goal):
    if goal not in prev and goal != start:
        return []
    path = [goal]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()
    return path
