from Graph import *
from Cola import *
class BreadthFirst:
    #G: graph
    #s: source
    def __init__(self, G):
        self.marked = [False]*G.getV()
        self.distTo = [float('inf') for _ in range(G.getV())]
        self.edgeTo = [None]*G.getV()
        self.G = G

    def bfs(self,s):
        #queue
        q = Cola()
        print(f"marked: {self.marked}")
        print(f"distTo: {self.distTo}")
        print(f"edgeTo: {self.edgeTo}")
        self.distTo[s] = 0
        self.marked[s] = True
        q.enqueue(s)

        while not q.isEmpty():
            v = q.dequeue()
            for w in self.G.getAdj(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.distTo[w] = self.distTo[v] + 1
                    self.marked[w] = True
                    q.enqueue(w)
        print(f"marked: {self.marked}")
        print(f"distTo: {self.distTo}")
        print(f"edgeTo: {self.edgeTo}")

if __name__ == '__main__':
    inp = "tinyCG.txt"
    G = Graph()
    G.load_from_file(inp)
    print(G)
    bfsO = BreadthFirst(G)
    bfsO.bfs(0)