import networkx as nx
import os
import random

def load_graph():
    """
    Load SNAP dataset into a directed NetworkX graph.
    Each line in file is 'u v'.
    - Uses roadNet-PA.txt if available
    - Otherwise falls back to sample_edges.txt
    """
    # Full dataset path
    pa_path = r"D:\google_route_opt\route-engine\data\roadNet-PA.txt"
    # Sample dataset path
    sample_path = "data/sample_edges.txt"

    # Pick dataset
    if os.path.exists(pa_path):
        file_path = pa_path
    else:
        file_path = sample_path

    G = nx.DiGraph()
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            u, v = map(int, line.strip().split())
            # Assign more realistic weights: short = 1–3, long = 7–10
            weight = random.choice([1, 2, 3, 7, 8, 9, 10])
            G.add_edge(u, v, weight=weight)

    print(f"Loaded graph from {os.path.basename(file_path)}: "
          f"{G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


if __name__ == "__main__":
    graph = load_graph()
    print(f" Graph loaded: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")
