## Formalizing approximation problems

### What is an NP-optimization problem?
![](pics/Pasted%20image%2020250105191608.png)
### What is the definition of approximation ratio?
The approximation ratio helps us measure how good our approximate solutions are compared to the optimal solution. For a minimization problem, if our algorithm produces a solution with value $A(I)$ for an instance I, and the optimal solution has value $OPT(I)$, then the approximation ratio is $\frac{A(I)}{OPT(I)}$. 
For maximization problems, we flip this to $\frac{OPT(I)}{A(I)}$. 
The key is that this ratio should be as close to 1 as possible - that's when our approximation is closest to optimal.

Min = $\alpha = \frac{APX}{OPT}$

Max = $\alpha = \frac{OPT}{APX}$

An algorithm with an approximation ratio $\alpha$ guarantees that the solution it produces is within a factor $\alpha$ of the optimal solution

### What is a PTAS and what is an FPTAS? Which one is more desirable in theory? Give examples for running times that match the definitions of PTAS and FPTAS algorithms.
**FPTAS** Fully Polynomial Time Approximation Scheme
- For every $\epsilon > 0$ there is a $poly(\epsilon^{-1},n)$ time algorithm with approximation ratio $\alpha = (1+\epsilon)$

Importantly, the run-time of an FPTAS is polynomial in the problem size and in 1/ε. This is in contrast to a general [polynomial-time approximation scheme](https://en.wikipedia.org/wiki/Polynomial-time_approximation_scheme "Polynomial-time approximation scheme") (PTAS). The run-time of a general PTAS is polynomial in the problem size for each specific ε, but might be exponential in 1/ε

**PTAS** Polynomial Time Approximation Scheme
- for every $\epsilon>0$ there is an $O(n^{f(1/ \epsilon)})$ time algorithm with approximation ratio $\alpha = (1+\epsilon)$

## Approximating vertex-cover

Describe the matching-based algorithm for finding a vertex-cover in a graph that is at most twice as large as the minimum vertex-cover. Include the following in your description:

### What does the existence of a k-edge matching imply for the minimum size of a vertex-cover?
### How does it matter whether you consider maximum matchings or maximal matchings in the algorithm? Which is the better choice?
### Give an infinite family of example graphs on which the algorithm indeed outputs only a 2-approximate solution. Also give a family of example graphs on which the algorithm outputs an optimal solution.
# Approximation algorithms
## Coloring 3-colorable graphs

### Given a 3-colorable n-vertex graph, show how you can in polynomial time find a proper $O(\sqrt{n})$-coloring of the graph
![](pics/Pasted%20image%2020250105185159.png)
We know the graph can be colored with 3 colors, 

The key insight comes from looking at independent sets in the graph. 
n a 3-colorable graph, at least one color class must contain at least $n/3$ vertices. This gives us our strategy: repeatedly find large independent sets and color them with new colors.

Here's how the algorithm works:

We start with the input graph and repeatedly:

1. Find a large independent set (of size at least Ω(√n))
2. Color all vertices in this set with a new color
3. Remove these vertices from the graph
4. Continue until the graph is empty

## Metric problems and TSP

### What does it mean that a graph has metric costs/weights?

### What is the Steiner Tree problem?
#### How can it be reduced to a version in which the input graph is required to have metric costs?
#### Give a 2-approximation for Metric Steiner Tree.

### Define the TSP and argue that it is NP-complete.
### Show that TSP remains NP-complete on metric instances.
### How do the general TSP and the metric TSP differ in terms of approximability? Argue that the general TSP cannot be approximated within a constant factor unless P=NP.
### Describe how to obtain a 2-approximation for the metric TSP. Highlight where you use the metric property.
###  Describe how to obtain a (3/2)-approximation for the metric TSP

## Semidefinite Programming

- [ ] math
### What is a semidefinite program? How fast can we find a solution to a semidefinite program in n variables?
###  For a positive semidefinite matrix M, what is the name of the algorithm that computes a triangular matrix L so that LL^T=M? What is its running time?
### Name two combinatorial problems that can be approximated with the help of semidefinite programming.
### How do you get from the vectors obtained from a solution to the semidefinite program to a solution to the combinatorial problem?
