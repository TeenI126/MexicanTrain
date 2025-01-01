from __future__ import annotations # allows class to reference self

class domino:
    left: int
    right: int
    adj: list[domino]

    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right
        self.adj = []
    
    def find_longest_chain(self, chain = []) -> list[domino]:
        
        # remove from adj doms already in chain
        adj_copy = self.adj.copy()
        for chained in chain:
            if chained in adj_copy:
                adj_copy.remove(chained)
        
        # base case: no more neighbours to explore
        if len(adj_copy) == 0:
            return chain + [self]

        # inductive step: find longest chain from each neighbour
        else:
            best_chain = []
            for neighbour in adj_copy:
                neighbour_chain = neighbour.find_longest_chain(chain + [self])
                if len(best_chain) < len(neighbour_chain):
                    best_chain = neighbour_chain
            return best_chain



    def __str__(self):
        return f"{self.left}:{self.right} -- {len(self.adj)}"

    def __repr__(self):
        return str(self)

    def __eq__(self, value : domino):
        return set([self.left, self.right]) == set([value.left, value.right])
    
class DominoGraph:
    doms: list[domino]

    def __init__(self):
        self.doms = []

    def add_domino(self, dom: domino):
        
        # see if new domino would be a neighbour with any existing dominos
        for d in self.doms:
            if dom.left in [d.left, d.right] or dom.right in [d.left, d.right]:
                d.adj.append(dom)
                dom.adj.append(d)
        
        self.doms.append(dom)
    
    def __str__(self):
        temp = ""
        for d in self.doms:
            temp += str(d) + "\n"
        return temp


mypieces : list[domino]

def find_chains(self, start: int):
    pass

if __name__ == "__main__":
    dominos = DominoGraph()

    print("enter tiles")
    while True:
        vals = input("\n")
        if vals is "":
            break
        vals = vals.split(" ")
        dom = domino(int(vals[0]), int(vals[1]))

        dominos.add_domino(dom)
    
    print(dominos)

    print(dominos.doms[0].find_longest_chain())

