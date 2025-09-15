from graph import load_graph
from algo import dijkstra, astar
from cache import cached_shortest_path, graph_to_tuple
import random
import time
import matplotlib.pyplot as plt
import networkx as nx

# Load Graph
graph_nx = load_graph()  # Automatically chooses sample or PA dataset

# Convert to adjacency list for algorithms
graph = {u: [(v, graph_nx[u][v]['weight']) for v in graph_nx.successors(u)] for u in graph_nx.nodes()}

print(f"Graph ready with {len(graph)} nodes")


# Pick connected start & goal nodes

# Use NetworkX connected components to ensure path exists
if nx.is_directed(graph_nx):
    components = list(nx.strongly_connected_components(graph_nx))
else:
    components = list(nx.connected_components(graph_nx))

# Pick a large component to avoid small isolated subgraphs
largest_comp = max(components, key=len)
nodes = list(largest_comp)

start = random.choice(nodes)
goal = random.choice(nodes)
while goal == start:
    goal = random.choice(nodes)

print(f"Testing shortest path from {start} to {goal}")


# Dijkstra and A* (uncached)

start_time = time.time()
path_dij, dist_dij = dijkstra(graph, start, goal)
end_time = time.time()
print(f"Dijkstra: distance={dist_dij}, path length={len(path_dij)}, time={end_time - start_time:.4f}s")

start_time = time.time()
path_astar, dist_astar = astar(graph, start, goal)
end_time = time.time()
print(f"A*: distance={dist_astar}, path length={len(path_astar)}, time={end_time - start_time:.4f}s")


# LRU Cache for repeated queries

graph_tuple = graph_to_tuple(graph)
dijkstra_cached = cached_shortest_path(dijkstra)
astar_cached = cached_shortest_path(astar)

print("\nRunning first Dijkstra query (cached wrapper)...")
start_time = time.time()
path_dij_c, dist_dij_c = dijkstra_cached(graph_tuple, start, goal)
end_time = time.time()
print(f"Dijkstra cached: distance={dist_dij_c}, path length={len(path_dij_c)}, time={end_time - start_time:.6f}s")

print("Running second Dijkstra query (should hit cache)...")
start_time = time.time()
path_dij_c2, dist_dij_c2 = dijkstra_cached(graph_tuple, start, goal)
end_time = time.time()
print(f"Dijkstra cached repeat: distance={dist_dij_c2}, path length={len(path_dij_c2)}, time={end_time - start_time:.6f}s")

print("\nRunning first A* query (cached wrapper)...")
start_time = time.time()
path_astar_c, dist_astar_c = astar_cached(graph_tuple, start, goal)
end_time = time.time()
print(f"A* cached: distance={dist_astar_c}, path length={len(path_astar_c)}, time={end_time - start_time:.6f}s")

print("Running second A* query (should hit cache)...")
start_time = time.time()
path_astar_c2, dist_astar_c2 = astar_cached(graph_tuple, start, goal)
end_time = time.time()
print(f"A* cached repeat: distance={dist_astar_c2}, path length={len(path_astar_c2)}, time={end_time - start_time:.6f}s")


# Linear Path-Only Visualization

plt.figure(figsize=(12, 3))

# Dijkstra path
dijkstra_x = list(range(len(path_dij)))
dijkstra_y = [1] * len(path_dij)
plt.plot(dijkstra_x, dijkstra_y, 'bo-', label='Dijkstra', markersize=5)

# A* path
astar_x = list(range(len(path_astar)))
astar_y = [2] * len(path_astar)
plt.plot(astar_x, astar_y, 'ro--', label='A*', markersize=5)

# Highlight start and goal
plt.text(0, 1, 'Start', color='green', fontsize=10, verticalalignment='bottom')
plt.text(len(path_dij)-1, 1, 'Goal', color='red', fontsize=10, verticalalignment='bottom')

plt.text(0, 2, 'Start', color='green', fontsize=10, verticalalignment='bottom')
plt.text(len(path_astar)-1, 2, 'Goal', color='red', fontsize=10, verticalalignment='bottom')

plt.yticks([1, 2], ['Dijkstra', 'A*'])
plt.xlabel("Step along path")
plt.title("Shortest Path Comparison: Dijkstra (blue) vs A* (red dashed)")
plt.legend()
plt.tight_layout()
plt.savefig("data/shortest_path_comparison.png", dpi=300, bbox_inches='tight')


