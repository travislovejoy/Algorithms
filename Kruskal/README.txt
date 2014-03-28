kruskal.py-Find the Minimum Spanning tree in a graph using the kruskal algorithm.

Code is based on psuedocode from textbook Introduction to Algorithms, Third edition by Cormen.

MST-Kruskal(G, w)  
//  
// Kruskal's algorithm
// 
A = emtpy                   // a subset of MST
for each vertex v in V 
    Make-set(v) 
endfor 
Sort the edges E in nondecreasing order by w
for each edge (u,v) in E    // taken in nondecreasing order by weight
    if Find-set(u) notequal Find-set(v) 
        A = A U {(u,v)} 
        Union(u,v) 
    endif 
endfor
return A

Sample input:
8
-1,11,9,6,-1,-1,-1,-1
11,-1,-1,5,7,-1,-1,-1
9,-1,-1,12,-1,6,-1,-1
6,5,12,-1,4,3,7,-1
-1,7,-1,4,-1,-1,2,-1
-1,-1,6,3,-1,-1,8,10
-1,-1,-1,7,2,8,-1,6
-1,-1,-1,-1,-1,10,6,-1

Output:
32
GE,FD,ED,DB,DA,FC,HG

