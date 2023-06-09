from Graph import *
class DepthFirstSearch:
    def __init__(self,G):
        self.G = G
        self.marked = [False]*G.getV()
        self.edgeTo = [None] * G.getV()
        self.count = 0

    def dfs(self,v):
        self.count += 1
        self.marked[v] = True
        for w in self.G.getAdj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(w)

    def show(self):
        print(f"marked: {self.marked}")
        print(f"edgeTo: {self.edgeTo}")

if __name__ == '__main__':
    inp = "tinyG.txt"
    G = Graph()
    G.load_from_file(inp)
    print(G)
    bfsO = DepthFirstSearch(G)
    bfsO.dfs(0)
    bfsO.show()