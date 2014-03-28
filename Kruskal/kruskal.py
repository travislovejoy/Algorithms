from string import ascii_uppercase


class Vertex:
    def __init__(self, number):
        self.number = number
        self.parent = self
        
    def findSet(self):
	#Parent signifies which set Vertex is in
        if self.parent != self:
            self.parent = self.parent.findSet()
        return self.parent

    def union(self, x):
	#Assign the two Vertexes the same parents.
        v1Parent = self.findSet()
        v2Parent = x.findSet()
        v1Parent.parent = v2Parent
            
class Edge:
    def __init__(self, v1, v2,weight):
	self.weight= weight
	self.v1= v1
	self.v2= v2

if __name__ == '__main__':
    number_of_vertices = int(raw_input())
    matrix = []
    for i in range(number_of_vertices):
        matrix.append([int(x) for x in raw_input().split(',')])
    edges=[]
    for x in range(number_of_vertices):
	for y in range(number_of_vertices):
		# if x==y then we are looking at edges you have already seen(undirected graphs)		
		if x==y: break
		if matrix[x][y]!=-1:
			edges.append(Edge(x,y,matrix[x][y]))	
     
    s = []
    vertices = []
    
    for i in range(number_of_vertices):
        vertices.append(Vertex(i))
    #Sort edges by weight
    for e in sorted(edges, key=lambda edge: edge.weight):
        #Check to see if new edge forms a cycle
	if vertices[e.v1].findSet()!=vertices[e.v2].findSet():
            s.append(e)
            vertices[e.v1].union(vertices[e.v2])
    print sum(e.weight for e in s)
    print ','.join(ascii_uppercase[e.v1]+ascii_uppercase[e.v2] for e in s)
