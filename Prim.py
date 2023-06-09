from ColaMin import ColaMin
from WeightedGraph import *
class Prim:
    def __init__(self):
        self.edgeTo = None #padres
        self.distTo = None #distancia
        self.marked = None #estado
        self.mcola = ColaMin() #cola
        self.G = None #Graph

    def PrimMST(self, G):
        self.G = G
        nv = self.G.getV()
        self.edgeTo = [None]*nv
        self.distTo = [float('inf')]*nv
        self.marked = [False]*nv
        print('---------------')
        print(self.distTo)
        print(self.marked)
        print(self.edgeTo)
        for i in range(nv):
            if not self.marked[i]:
                self.prim(i)#minimum spanning forest
        print('---------------')
        print(self.distTo)
        print(self.marked)
        print(self.edgeTo)
    def prim(self,s):
        self.distTo[s]=0.0
        self.mcola.enqueue(s,self.distTo[s])
        while not self.mcola.isEmpty():
            u, d = self.mcola.delMin()
            self.marked[u] = True
            for vx in self.G.getAdj(u):
                v = vx.getOther(u)
                if self.marked[v]:
                    continue
                if vx.getWeight() < self.distTo[v]:
                    self.distTo[v] = vx.getWeight()
                    self.edgeTo[v] = u

                    if self.mcola.isInQueue(v):#udpate queue
                        self.mcola.updateKey(v,self.distTo[v])
                    else:#insert in queue
                        self.mcola.enqueue(v,self.distTo[v])

if __name__ == '__main__':
    inp = "tinyEWGP.txt"
    G = WeightedGraph()
    G.load_from_file(inp)
    print(G)
    pr = Prim()
    pr.PrimMST(G)
