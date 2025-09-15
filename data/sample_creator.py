import random

infile = "data/roadNet-PA.txt"
outfile = "data/sample_edges.txt"
target_nodes = 50000

nodes = set()
with open(infile, "r") as fin, open(outfile, "w") as fout:
    for line in fin:
        if line.startswith("#"):
            continue
        u, v = line.split()
        u = int(u); v = int(v)
        if len(nodes) < target_nodes or (u in nodes or v in nodes):
            nodes.add(u); nodes.add(v)
            fout.write(f"{u} {v}\n")
        if len(nodes) >= target_nodes and random.random() > 0.99:
            break

print("Sample written to", outfile, "with", len(nodes), "nodes")
