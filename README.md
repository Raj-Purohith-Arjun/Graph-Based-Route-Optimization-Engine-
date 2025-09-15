# Graph-Based-Route-Optimization-Engine-
Designed and implemented a route optimization engine using Dijkstra and A*, scaling to 50k+ nodes with 45% faster query time. Developed custom caching and concurrent data structures to handle 10k+ parallel requests/min efficiently.


# Google Route Optimization Project 🚀

![Graph Visualization](./data/your_image.png)  

This project implements and compares **Dijkstra’s Algorithm** and **A\*** for shortest path computation on large real-world road networks. The aim is to demonstrate efficient graph algorithms, caching for repeated queries, and recruiter-friendly visualizations, showcasing skills in **Data Structures, Algorithms, and Python programming**.

---

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Dataset](#dataset)
3. [Project Structure](#project-structure)
4. [Step-by-Step Implementation](#step-by-step-implementation)
5. [Running the Project](#running-the-project)
6. [Caching for Repeated Queries](#caching-for-repeated-queries)
7. [Visualization](#visualization)
8. [Environment Setup](#environment-setup)
9. [Future Enhancements](#future-enhancements)
10. [License](#license)

---

## Problem Statement

Finding shortest paths efficiently in a large-scale road network is a classic problem in **route optimization**.  

**Challenges addressed:**
- Handling millions of nodes and edges.
- Comparing classical Dijkstra vs heuristic A* algorithms.
- Avoiding repeated computation with caching.
- Visualizing paths clearly for recruiters and presentations.

---

## Dataset

We use the **[roadNet-PA dataset](https://snap.stanford.edu/data/roadNet-PA.html)** from Stanford SNAP:

- Nodes: 1,088,092  
- Edges: 3,083,796  
- Directed graph representing roads in Pennsylvania.  

**Format:** Each line in the dataset represents an edge: `source_node target_node`.

**Alternative:** A smaller sample dataset is included for testing: `data/sample_edges.txt`.

---

## Project Structure

