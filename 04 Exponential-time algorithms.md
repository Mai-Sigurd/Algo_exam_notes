## ETH and SETH

- [ ] check for math
- Explain the statement of the exponential-time hypothesis ETH and the strong exponential-time hypothesis SETH. Consider the following:
  - Why do they imply P != NP?
  - Is an algorithm with running time for 3-SAT possible under ETH?𝑂(1. 0001𝑛) ○ Is an algorithm with running time for 3-SAT possible under ETH?𝑂(1001𝑛/𝑙𝑜𝑔 𝑛)
  - Are either of these algorithms possible under SETH?
  - Briefly give two examples for concrete super-polynomial running times for 3-SAT that are ruled out under ETH.
- What is the sparsification lemma, and why is it useful?
- Describe the Orthogonal Vectors problem.
  - Which lower bound does SETH yield for this problem? Sketch the lower bound.
  - Is an algorithm or an time algorithm possible under𝑂(𝑛2/ log 𝑛) 𝑂(𝑛2/ 𝑛) SETH?
- Describe the k-Dominating Set problem. ○ Which lower bound does SETH yield for this problem? Sketch the lower bound

## Inclusion/Exclusion

- [ ] check for math

- State and explain the inclusion-exclusion principle.
- Describe how to solve the Hamiltonian cycle problem using inclusion-exclusion.
  - Describe the role of walks and paths.
  - How can you count walks in polynomial time?
  - Why do you need to count them, and why is deciding existence not enough?
  - Briefly compare this approach to the Bellman-Held-Karp dynamic programming algorithm for Hamiltonian cycles. Also outline the DP algorithm.
- Describe how to count perfect matchings in a graph using inclusion-exclusion. Which structures are counted in the individual terms of the inclusion-exclusion formula? How can you speed this up on bipartite graphs, and what are the structures counted there?
- Consider an n-vertex graph G.
  - How is the chromatic number of G defined?
  - How can you compute the chromatic number in time? The approach𝑂(3𝑛) we’ve studied reduces the problem to counting certain structures. What are these structures and how fast can you count them?
