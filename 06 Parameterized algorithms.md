
## Basics and Branching

### What is a parameterised problem?

A paramitized problem is a problem with an additional input typically. For example in the vertex cover, we give the input and a k, where k is the size of the cover we want to find.

### What is an FPT algorithm?

An FPT, fixed parameter tractable, algo that solves a problem in time
$$F(k) \cdot poly(|I|)$$
Where f(k) is function only dependent onk
poly in input size
FPT algorithms are considered efficient for small values of k because the dependence on $k$ is separated from the input size, and the running time is polynomial in $|I|$ for a fixed $k$.

### For which parameter choices does an FPT algorithm run in polynomial time?

An FPT algorithm runs in polynomial time when the parameter k is bounded by a constant. In such cases, the function f(k) becomes a constant multiplier, and the overall running time simplifies to, poly(I) which is polynomial.

### Describe how to solve the Vertex Cover problem in running time, where k is the$𝑂(2^{𝑘}𝑛)$ solution size.

### How can you improve the running time of the above algorithm?

### How can we solve Independent Set on 3-regular graphs in time $𝑂(4^{𝑘}𝑛)$ ?

### Define a tournament. How can we solve Feedback Vertex Set on Tournaments in time $O(3^{k}n^{3})$?

## Kernelization

- [ ] check for math

### What is a kernel for a parameterized problem?

### Argue that a parameterized problem has a kernel if and only if it is FPT

### What is a polynomial kernel?

### Give a kernel for Vertex Cover parameterized by the solution size k with vertices𝑂(𝑘2)

### Define the Edge Clique Cover problem. Give a kernel for Edge Clique Cover parameterized by the solution size k. Is this a polynomial kernel?

## Treewidth

- [ ] check for math

### Define the treewidth of a graph. Give examples for graph families with small and large treewidth (without proofs). Sketch the tree-decomposition for a grid.

### What is a nice tree-decomposition? Why is it useful?

### Describe how to solve the Maximum Independent Set problem on graphs of bounded treewidth.

#### What running time do you achieve?

#### Describe what information you store and how it is computed at the nodes of the tree-decomposition from previously computed information.

#### How to use this to conclude Vertex Cover is FPT parameterized by treewidth?

### Describe how to solve the 3-coloring problem on graphs of bounded treewidth.

### Describe how to solve the MaxCut problem on graphs of bounded treewidth.

### Describe the idea of a win-win approach to design parameterized algorithms.

### What does it mean that H is a minor of G? What does the Excluded Grid Minor Theorem say? How is it helpful to the win-win approach?

### What does the Planar Excluded Grid Minor Theorem say? How is it helpful to design subexponential parameterized algorithms on planar graphs? (Recall, in this case subexponential algorithms are those with running time where k is the2𝑂( 𝑘)𝑛𝑂(1) solution size.

### How can we solve Vertex Cover and k-Path in time on planar graphs?

## Color-coding

- [ ] check for math

### Describe the “color-coding” algorithm for deciding whether a graph has a path of length k.

Make sure to explain the role of random colorings and walks. What changes if you want to decide the existence of cycles rather than paths?

### How can you determine the existence of a colorful k-path in a vertex-colored graph in time or ? (For the second running time, modify the DP for(𝑘 + 1)! · 𝑛𝑂(1) 2𝑘𝑛𝑂(1) Hamiltonian paths.)
