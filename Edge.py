class Edge:
    def __init__(self,v,w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    def getWeight(self):
        return self.weight
    def getVEnd(self):
        return  self.v
    def getV(self):
        return self.v
    def getW(self):
        return self.w
    #complement
    def getOther(self, vx):
        if vx == self.v:
            return self.w
        elif vx == self.w:
            return self.v
        else:
            return -1
    def compareTo(self,O):
        if self.getW() < O.getWeight():
            return -1
        elif self.getW() > O.getWeight():
            return 1
        else:
            return 0
    def __str__(self):
        s = "({}-{} {})".format(self.getV(),self.getW(),self.getWeight())
        return s

"""
if __name__=='__main__':
    e = Edge(12,34,5.67)
    print(e)
"""