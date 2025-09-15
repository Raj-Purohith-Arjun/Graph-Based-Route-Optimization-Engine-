from functools import lru_cache


# Cache wrapper for shortest path

def cached_shortest_path(func):
    """
    LRU cache decorator for shortest path functions.
    Caches up to 1024 unique (start, goal) queries.
    """
    @lru_cache(maxsize=1024)
    def wrapper(graph_tuple, start, goal):
        # Convert tuple back to dict inside function
        graph = {u: [(v, w) for v, w in edges] for u, edges in graph_tuple}
        return func(graph, start, goal)
    return wrapper


# Helper to convert dict graph to tuple (hashable for caching)
def graph_to_tuple(graph):
    """
    Convert adjacency dict to tuple of tuples for caching.
    """
    return tuple((u, tuple(edges)) for u, edges in graph.items())
