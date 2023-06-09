class ColaMin:
  def __init__(self):
    self.items = []#vertices
    self.keys = []#distancia

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item, key):
    self.items.insert(0,item)
    self.keys.insert(0,key)

  def dequeue(self):
    return (self.items.pop(), self.keys.pop())

  def size(self):
    return len(self.items)

  def delMin(self):
      val = min(self.keys)#distancia minima
      idx = self.keys.index(val)
      rt = self.items[idx]#vertice
      #delete vertex
      self.keys.pop(idx)
      self.items.pop(idx)
      return rt,val #vertex, distance

  def isInQueue(self, v):
      for i in self.items:
          if i == v:
              return True
      return False

  def updateKey(self,w, key):
      for ix,val in enumerate(self.items):
          if val == w:
              self.keys[ix] = key