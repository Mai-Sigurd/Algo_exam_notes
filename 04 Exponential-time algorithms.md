## ETH and SETH

### Explain the statement of the exponential-time hypothesis ETH and the strong exponential-time hypothesis SETH. Consider the following:
The Exponential Time Hypothesis (ETH) states that 3-SAT cannot be solved in subexponential time, specifically that it requires at least $2^{cn}$ time for some constant $c > 0,$ where $n$ is the number of variables

**ETH**:  $\exists S >0$ such that 3-sat requires time $\geq 2^{sn}$

**Seth** : $\forall s >0,$ $\exists k$ s.t k-sat requires $2^{(1-s)n}$ time
#### Why do they imply $P \neq NP$?
ETH implies $P \neq NP$ because if $P = NP$, all NP problems, including 3-SAT, would be solvable in polynomial time, contradicting ETH.
==TODO help==
#### Is an algorithm with running time $O(1.0001^{n})$ for 3-SAT possible under ETH? 

#### Is an algorithm with running time $O(1001^{{n}/{\log n}})$ for 3-SAT possible under ETH?
#### Are either of these algorithms possible under SETH?
#### Briefly give two examples for concrete super-polynomial running times for 3-SAT that are ruled out under ETH.
### What is the sparsification lemma, and why is it useful?
The sparsification lemma states that any CNF formula $\phi$ with $n$ variables and $m$ clauses can be written as a disjunction of $O(2^{\epsilon n})$ CNF formulas, each with $O(n / \epsilon)$ clauses, for any $\epsilon > 0$
### Describe the Orthogonal Vectors problem.
#### Which lower bound does SETH yield for this problem? Sketch the lower bound.
#### Is an $O(n^{2}/\log n)$ algorithm or an $O(n^{2} / \sqrt{n})$ time algorithm possible under SETH?
### Describe the k-Dominating Set problem. 
#### Which lower bound does SETH yield for this problem? Sketch the lower bound

## Inclusion/Exclusion

### State and explain the inclusion-exclusion principle.
![](pics/inclusion2.png)![](pics/inclusion3.png)
### Describe how to solve the Hamiltonian cycle problem using inclusion-exclusion.
#### Describe the role of walks and paths.
#### How can you count walks in polynomial time?
#### Why do you need to count them, and why is deciding existence not enough?
#### Briefly compare this approach to the Bellman-Held-Karp dynamic programming algorithm for Hamiltonian cycles. Also outline the DP algorithm.
### Describe how to count perfect matchings in a graph using inclusion-exclusion. Which structures are counted in the individual terms of the inclusion-exclusion formula? How can you speed this up on bipartite graphs, and what are the structures counted there?

### Consider an n-vertex graph G.
#### How is the chromatic number of G defined?
![](pics/chromatic.png)
#### How can you compute the chromatic $O(3^{n})$ number in time? The approach we’ve studied reduces the problem to counting certain structures. What are these structures and how fast can you count them?
- Every colorclass is an indpendent set in the graph. 
- Let the ground set 𝑈 be the set of vertices 𝑉. 
- Let the family ℱ be the independent sets in the graph. 
- To see if 𝑘 colors are enough, we want to see if 𝑈 can be covered by 𝑘 independent sets. 
- The smallest such 𝑘 is the chromatic number

==TODO RUNTIME==
![](pics/chromaticalog.png)