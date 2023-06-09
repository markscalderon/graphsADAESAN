from Edge import Edge
class WeightedGraph:
    def __init__(self):
        self.V = 0
        self.E = 0
        self.adj = None

    def load_from_file(self, path):
        with open(path) as f:
            self.V = int(f.readline())
            self.adj = [[] for _ in range(self.V)]
            self.E = int(f.readline())
            for i in range(self.E):
                s = f.readline()

                s = s.replace('\n','')

                L = s.split(' ')
                v = int(L[0])
                w = int(L[1])
                wg = float(L[2])
                if self.validateVertex(v) and self.validateVertex(w):
                    E = Edge(v,w,wg)
                    self.addEdge(E)

    def getV(self):
        return self.V
    def getE(self):
        return self.E
    def getAdj(self,v):
        return self.adj[v]
    def validateVertex(self, v):
        if v < 0 or v >= self.V:
            return False
        else:
            return True

    def addEdge(self, E):
        v = E.getV()
        w = E.getW()
        if self.validateVertex(v) and self.validateVertex(w):
            self.adj[v].append(E)
            self.adj[w].append(E)

    def __str__(self):
        s = ""
        for i in range(self.V):
            s = s + str(i) + ": "
            L = self.adj[i]

            for j in L:
                s = s + j.__str__() +","
            s = s + '\n'
        return s

"""
if __name__ == '__main__':
    inp = "tinyEWG.txt"
    G = WeightedGraph()
    G.load_from_file(inp)
    print(G)
"""