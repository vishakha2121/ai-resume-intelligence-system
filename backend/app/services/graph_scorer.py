import networkx as nx
import re

def build_graph(resume_text, jd_text):
    G = nx.Graph()
    # Extract words as nodes (simplified)
    resume_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', jd_text.lower()))
    common = resume_words.intersection(jd_words)
    for w in common:
        G.add_node(w)
    # Add edges between words that co-occur in same sentence (simplified)
    # Not fully implemented for brevity; just return a small graph
    for w1 in list(common)[:5]:
        for w2 in list(common)[:5]:
            if w1 != w2:
                G.add_edge(w1, w2)
    return G

def compute_page_rank(G):
    if len(G.nodes) == 0:
        return 0.5
    pr = nx.pagerank(G)
    return sum(pr.values()) / len(pr) if pr else 0.5