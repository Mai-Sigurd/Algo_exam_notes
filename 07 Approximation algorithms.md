## Formalizing approximation problems

- What is an NP-optimization problem?
- What is the definition of approximation ratio?
- What is a PTAS and what is an FPTAS? Which one is more desirable in theory? Give examples for running times that match the definitions of PTAS and FPTAS algorithms.

## Approximating vertex-cover

Describe the matching-based algorithm for finding a vertex-cover in a graph that is at most twice as large as the minimum vertex-cover. Include the following in your description:

- What does the existence of a k-edge matching imply for the minimum size of a vertex-cover?
- How does it matter whether you consider maximum matchings or maximal matchings in the algorithm? Which is the better choice?
- Give an infinite family of example graphs on which the algorithm indeed outputs only a 2-approximate solution. Also give a family of example graphs on which the algorithm outputs an optimal solution.

## Coloring 3-colorable graphs

- [ ] math

* Given a 3-colorable n-vertex graph, show how you can in polynomial time find a proper O(sqrt(n))-coloring of the graph

## Metric problems and TSP

What does it mean that a graph has metric costs/weights?

- What is the Steiner Tree problem?
  - How can it be reduced to a version in which the input graph is required to have metric costs?
  - Give a 2-approximation for Metric Steiner Tree.

* Define the TSP and argue that it is NP-complete.
* Show that TSP remains NP-complete on metric instances.
* How do the general TSP and the metric TSP differ in terms of approximability? Argue that the general TSP cannot be approximated within a constant factor unless P=NP.
* Describe how to obtain a 2-approximation for the metric TSP. Highlight where you use the metric property.
* Describe how to obtain a (3/2)-approximation for the metric TSP

## Semidefinite Programming

- [ ] math
- What is a semidefinite program? How fast can we find a solution to a semidefinite program in n variables?
- For a positive semidefinite matrix M, what is the name of the algorithm that computes a triangular matrix L so that LL^T=M? What is its running time?
- Name two combinatorial problems that can be approximated with the help of semidefinite programming.
- How do you get from the vectors obtained from a solution to the semidefinite program to a solution to the combinatorial problem?
