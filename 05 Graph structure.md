
# Chordal graphs 
### What is a chordal graph and what is an interval graph? 
**Chordal graph**, example, where all cycles can be broken down into cycles of 3. There has to be a chord in the cycle if it is a above 3. 
**Interval graph**
An interval graph is a graph that has an interval model and it is a type of chordal graph.
As it cannot have cycles with no chord. 
As we can see in example of C4. Drawing
### Show that every interval graph is a chordal graph. 
Well in particicluar, this is shown by the cycle constraint. If we have a a C4. We cannot order them linearly, as we would like to when we have a interval graph. This introduces thee needs for chords, thus making it a chordal graph. 
- [ ] ==TODO: Would be good with drawing==

### Show that a graph is chordal if and only if it has a perfect elimination ordering. 
A perfect elimnation ordering is an ordering of the interval or chordal graph that, 

> [!DEF]
> A perfect elimination ordering is an ordering of $V(G)$  $V_{1}V_{2}V_3...V_{n}$ s.t
> the neighbors of $V_i$ in $G[{V_{1},V_{2},V_3,...,V_{i-1}}]$ form a clique. 
> $G[{V_{1,}V_{2},V_3,...,V_{i-1}}]$ : subgraph of G indueces by the set ${V_{1},V_{2},V_3,...,V_{i-1}}$

Inteval graphs have a PEO, but some non interval graphs also have a peo. 
> [!DEF]
> **N(V)**: Set of vertices adjacent to V, neighbourhood
> **Simplicial vertex**: If N(v) is a clique in G. Then v is a simplicial vertex


##### non interval with peo
![[pics/Pasted image 20241226111541.png]]
##### continue
**Observation 1** : With the peo defined we can make the observation that, the cycle graph $CI$ for i larger than 4, does not a peo, because CI does not have any simplicial vertcies
**Observation2**: If a graph has Ci as an induced subgraph, then it does not have a peo. 
proof with Íwith drawing
![[pics/Pasted image 20241226120534.png]]
#### 

#### Chordal graph <= peo
In oberservation 2 we show that if G is not chordal then it does not have a peo. 

#### Chordal => peo
- Let $G$ be a chordal graph. We want to show that G has a peo. 
- Note that for any vertices v, G-v is till chordal, as the removal of a vertex does not create any new cycles. 
- If g is chordal then it has atleast one simplicial vertex, and we can remove these vertices one by one, from G to obtain a perfect eliminiation ordering. 

- If G is a complete graph, then it has a simplicial vertex (a graph in which each vertex is connected to every other vertex)

- If G is not a complete graph. Then G has two non-adjacent simplicial vertices. We need:
	- A seperator in Graph G is a set $S \subseteq V(G)$ such that $G-S$ is disconnedted
	- A seperator is minimal if  no subset of S has the same property
	- ![[pics/Pasted image 20241226124415.png]]
**Proof** for the **lemma**
> [!Lemma]
> If G is chordal then any minimal seperator is a clique. 

Let S be a minimal separator of G and suppose by a contradiction that S is not a clique, That is $\exists u,v \in S$ st. $uv \notin E(G)$ 
By the minimality of S there exists two connected components $A,B$ of $G-S$ s.t every vertex of S has a neighbor in A and a neighbor in B 
S is a seperator => there are no edges between A and B
	Since A is a connected component and both u and v have a neighbor in A, $A \cup {u,v}$ is also connected 
	![[pics/Pasted image 20241226134717.png]]
	- Let $P_a$ be the shortest path between u and v in $G[{A\cup \{u,v\}}]$.
	- Let $P_b$ be a shortest u,v path defined anlogously in $G[{B\cup \{u,v\}}]$
	- Then since P_A has atleast one vertex in A and PB has at least one vertex in B then we conclude G has an induced cycle on at least 4 vertices. 
	==UNDERSTANDED! because m and v are missing a edge, they are therefore missing a chord
	

> [!Lemma]
> If $G$ is chordal and is not a clique then G has at least two non-adjacent simplicial vertices

**Proof**
We prove by induction on the number of vertices.
If G is not complete, G has at least three vertices. If G is a 3 vertices line (smallest non complete graph), then g has two non adjacent simplicial vertices. 
- Let G be a chordal graph that is not complete. 
	- Then $\exists x,y \in V(G)$ s.t $xy \notin E(G)$ 
- Let S be a minimal separator that separates x and y
- let A_x be the connected component of G-s that contains X and let A_y be defined accordingly. 
- ![[pics/Pasted image 20241226143953.png]]
	- Note that $G[A_{x}\cup S]$ is chordal . If $G[A_{x}\cup S]$ is complete, then A_x contain a simplicial vertex which is also a simplicial vertex in G. By induction hypothesis, $G[A_{x}\cup S]$ has two non-adjacent simplicial vertices. 
- note that a vertex that is simplicial in $G[A_{x}\cup S]$ but is contained in S is *not* necesarily simplicial in G, as  this vertex has neighboors in A_y .
  However since $G[A_{x}\cup S]$ has two non-adjacent simplicial vertices and by Obs2 S is a clique we know that at least one of the simplical vertices is in Ax, (and not in S) . Hence this vertex is also a simplicial in G. (Note that is has the same set of neighbors in $G[A_{x}\cup S]$ and in $G$
With a symetric argument we find a simplicial vertex in A_Y since S is a seperator, there are no edges between Ay and Ax. Hence we have found two-non adjacent simplicial in G as desired

By the main thm we conclude that GRAPH coloruong can be solved in poly time on chordal graphs. 

###  Give a polynomial time algorithm to solve the Graph Coloring problem on chordal graphs. Argue for the correctness of the algorithm. What is the running time? 
something something PEO?
### What is a clique tree for a chordal graph? Show how to construct a clique tree for a chordal graph in polynomial time.
A clique tree for a chordal graphs shows us the maximal sizes of the cliques, and the denotes for us some seperators.
We can construct these in polynomial time. 
![[pics/Pasted image 20241226153129.png]]

# Solving problems on chordal graphs 
###  Describe how to solve the Maximum Independent Set problem on trees. How can you solve it on forests?

###  What is a nice clique tree? 

### Describe the Feedback Vertex Set problem. Give a polynomial time algorithm to solve this problem on chordal graphs using a nice clique tree. What is the running time of the algorithm?