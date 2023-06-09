import time
class Graph:
    def __init__(self):
        self.V = 0 #number of vertices
        self.E = 0 #number of edges
        self.adj = None #list per vertices

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
                if self.validateVertex(v) and self.validateVertex(w):
                    self.addEdge(v,w)

    def addEdge(self,v,w):
        if self.validateVertex(v) and self.validateVertex(w):
            self.E += 1
            self.adj[v].append(w)
            self.adj[w].append(v)

    def validateVertex(self, v):
        if v < 0 or v >= self.V:
            return False
        else:
            return True

    def getV(self):
        return self.V
    def getE(self):
        return  self.E
    def getAdj(self,v):
        return self.adj[v]
    def degree(self,v):
        return len(self.adj[v])

    def __str__(self):
        s = ""
        n = self.getV()
        for i in range(n):
            s = s + str(i)+": "
            for j in self.adj[i]:
                s = s + str(j)+" "
            s = s + '\n'
        return s

if __name__ =="__main__":
    inp = "largeG.txt"
    G = Graph()
    st = time.time()
    G.load_from_file(inp)
    ed = time.time()
    print(ed-st)
    #print(G)