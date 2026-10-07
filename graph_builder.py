import networkx as nx
from pyvis.network import Network
import tempfile

def create_knowledge_graph(triples):
    G = nx.DiGraph()
    
    for subj, pred, obj in triples:
        G.add_node(subj, title=subj, color="#1f77b4")
        G.add_node(obj, title=obj, color="#aec7e8")
        G.add_edge(subj, obj, label=pred, title=pred)
        
    net = Network(height="450px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)
    net.from_nx(G)
    net.repulsion(node_distance=120, central_gravity=0.3, spring_length=100)
    
    # Save network as HTML temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
        net.save_graph(tmp_file.name)
        return tmp_file.name