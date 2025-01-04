
## Matrix multiplication 
### Define the matrix multiplication problem. How many arithmetic operations do you need to solve this problem in the standard way? 
You need 

|     | A   |
| --- | --- |
| B   | C   |
![[pics/dd.png]]
$O(n^3)$
### Describe a way to reduce $𝑛 × 𝑛$  matrix multiplication recursively to 8 multiplications of $𝑛/2 × 𝑛/2$ matrices.
![[pics/ddd.png]]
![[pics/IMG_2702.jpeg|500]]
red dot involves multiplying matrixes of size n/2
We branch out 8 times, ie red dots
so A = 8
b = 2
$n^2$ because we need to add the matrixes together 
$$T(n)= 8 \cdot T(\frac{n}{2})+O(n^2)$$
Solve with master thm
$\in \theta (n^3)$ 

### How many recursive multiplications does Strassen's algorithm require, and what running time does this translate to in the end? Argue for the running time bound. 
Strassens requires 7

$$O(n^{log_27})=O(n^{2.8}), \text{which dominates}O(n^2)$$

![[pics/IMG_2704.jpeg]]


### Define the constant $\omega$ . What does the existence of Strassen's algorithm imply for $\omega$ ? What are the best known lower and upper bounds on $\omega$?
>[!Def]
>$\omega$ : best known exponent $n^\omega$ for matrix multiplication

Trivial: $n^3$
Strassen: $n^{2.8}$
Lowest possible bound: $n^2$, because of the input size
somebody is out on the digits $2 \leq 2.3715 \leq 2.3728$
## Matrix multiplication for cliques
### How can matrix multiplication be used for detecting and counting triangles? 
We start by representing the graph trough an adjencency matrix.
When we times the matrix with it self, $A^2$
	![[pics/ggfbg.png]]
	We get a contribution of one for each index $k$ where there is an edge $ik$ as well as an edge $kj$—in other words, the $(i, j)$th entry of $A^2$ counts the number of two-hop paths from $i$ to $j$
	The diagonal entries $A^3[i][i]$ give three times the number of triangles involving vertex iii, as each triangle is counted once for each of its vertices.
	And twice for going around one way or the other
	so you divide the trace by 6

### How can the algorithm for triangles be extended to detect cliques of a given size k? How does this compare to the brute-force algorithm? 
A clique of size $k$ is a set of  $k$ vertices that are pairwise connected. Detecting or counting such cliques can be extended from the triangle-detection approach.

**Adjacency Matrix Representation**:
- Represent the graph with its adjacency matrix A, where $A[i][j]=1$ if there's an edge between vertices i and j, and 0 otherwise.
**Matrix Exponentiation**:
- Compute the matrix$A^{k-1}$ the $(k−1)$th power of the adjacency matrix. The entry $A^{k-1}[i][j]$ represents the number of walks of length $k−1$ from vertex i to vertex j.
**Clique Detection**:
- A k-clique involves k vertices that are all pairwise connected. For a set of vertices $\{v_1, v_2, \ldots, v_k\}$ to form a clique, each pair $(v_i, v_j)$ must have an edge between them.
- By analyzing the entries of $A^{k-1}$, we can infer the presence of k-cliques. Specifically, if $A^{k-1}[i][j]$ is non-zero, it indicates that there are paths connecting vertex i to vertex j through $k−2$ intermediate vertices, suggesting potential k-cliques.
**Verification**:
    - After identifying candidate sets of vertices from $A^{k-1}$ , verify that all pairs within each set are connected by checking the corresponding entries in the original adjacency matrix A.

![[pics/vfsvs.png]]
*from chat*
### Can you use the clique algorithm to find/count independent sets
The independent set is the opposite problem of the clique. 
**Key Insight**
An independent set in a graph is a set of vertices with no edges between them. A clique in the complement graph (where edges exist between non-adjacent vertices of the original graph) corresponds to an independent set in the original graph.

Find the complement graph $\overline{A} = J - I - A$ *dont know about this its from the chat*where J is the all-ones matrix and I is the identity matrix.

**Flip the matrix**
- Use the clique-detection algorithm on $\overline{A}$ to find cliques of size k in the complement graph.
- Each clique of size k in the complement graph corresponds to an independent set of size k in the original graph.