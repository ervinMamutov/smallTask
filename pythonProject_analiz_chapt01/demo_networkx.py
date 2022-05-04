# coding: utf8
# Chap01/demo_networkx.py
import networkx as nx
from datetime import datetime

if __name__ == '__main__':
    g = nx.Graph()

    g.add_node("Джон", {'имя': 'Джон', 'возраст': 25})
    g.add_node("Питер", {'имя': 'Питер', 'возраст': 35})
    g.add_node("Мэри", {'имя': 'Мэри', 'возраст': 31})
    g.add_node("Люси", {'имя': 'Люси', 'возраст': 19})

    g.add_edge("Джон", "Мэри", {'начиная с': datetime.today()})
    g.add_edge("Джон", "Питер", {'начиная с': datetime(1990, 7, 30)})
    g.add_edge("Мэри", "Люси", {'начиная с': datetime(2010, 8, 10)})

    print(g.nodes())
    print(g.edges())
    print(g.has_edge("Люси", "Мэри"))


    