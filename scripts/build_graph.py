#!/usr/bin/env python3
"""从 wiki/ 的 [[链接]] 生成关系图谱数据 docs/graph.json。
用法：在仓库根目录运行  python3 scripts/build_graph.py
"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
OUT  = os.path.join(ROOT, "docs")
os.makedirs(OUT, exist_ok=True)

link_re = re.compile(r'\[\[([^\]]+)\]\]')
nodes, order = {}, []
for sub, typ in [("实体", "entity"), ("概念", "concept"), ("来源", "source")]:
    for p in sorted(glob.glob(os.path.join(WIKI, sub, "*.md"))):
        base = os.path.splitext(os.path.basename(p))[0]
        nid = f"{sub}/{base}"
        with open(p, encoding="utf-8") as f:
            txt = f.read()
        m = re.search(r'^#\s+(.+)$', txt, re.M)
        nodes[nid] = {"type": typ, "label": m.group(1).strip() if m else base}
        order.append(nid)

def norm(t):
    return t.split("|")[0].split("#")[0].strip()

edges = set()
for nid in order:
    sub, base = nid.split("/", 1)
    with open(os.path.join(WIKI, sub, base + ".md"), encoding="utf-8") as f:
        for m in link_re.finditer(f.read()):
            tgt = norm(m.group(1))
            if tgt in nodes and tgt != nid:
                edges.add(tuple(sorted((nid, tgt))))

idx = {nid: i for i, nid in enumerate(order)}
deg = [0] * len(order)
for a, b in edges:
    deg[idx[a]] += 1
    deg[idx[b]] += 1

tmap = {"entity": "e", "concept": "c", "source": "s"}
graph = {
    "nodes": [{"id": i, "n": nodes[n]["label"], "t": tmap[nodes[n]["type"]], "v": deg[i]}
              for i, n in enumerate(order)],
    "links": [{"source": idx[a], "target": idx[b]} for a, b in sorted(edges)],
}
with open(os.path.join(OUT, "graph.json"), "w", encoding="utf-8") as f:
    json.dump(graph, f, ensure_ascii=False, separators=(",", ":"))
print(f"{len(graph['nodes'])} nodes, {len(graph['links'])} links -> docs/graph.json")
