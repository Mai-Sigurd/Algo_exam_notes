monomials is **an expression that has a single term, with variables and a coefficient**. For example, $2xy$ is a monomial since it is a single term, has two variables, and one coefficient. $2xy+10$ is a binomial
![](pics/vdss.png)

## Polynomial identity testing

### What is the polynomial identity testing problem?

A degree d polynomial has at most d roots
if a polynomial p is not identically zero, then $p(x)=0$ for at most d different x
The **polynomial identity testing (PIT)** problem asks whether a given polynomial $p(x_1, x_2, \dots, x_n)$ is identically zero. That is, it checks if $p \equiv 0$ across all possible input values.

Identity testing is the problem of determining whether a given multivariate [polynomial](https://en.wikipedia.org/wiki/Polynomial "Polynomial") is the 0-polynomial

![](pics/vsds.png)

### Why can it be reduced to deciding whether a given polynomial is the zero polynomial?

A polynomial is zero if and only if all its coefficients are zero. Testing whether $p(x) = 0$ for all $x$ reduces to verifying if p evaluates to zero for sufficiently many points. If p evaluates to nonzero at any point, it is not identically zero.

==TODO:snak med albert==

### Assume black-box access to a polynomial $p$ of degree at most $n$:

You can choose a query point $s$ and get back $p(s)$ as the result of your query.

#### How many points do you have to query in the worst-case in order to find out whether $p$ is the zero polynomial?

do we know the amount of roots? because if so then
In the black-box model, p has degree
$\leq d$. By the **fundamental theorem of algebra**, a nonzero polynomial of degree d has at most d roots. To guarantee detecting a nonzero polynomial, query $p(s)$ at $d+1$ distinct points. If $p(s) = 0$ for all such points, $p \equiv 0$.
If $d$ is unknown, the testing strategy would need to be adjusted, such as by testing over increasingly large sets of evaluation points until sufficient confidence is reached that $p \equiv 0$

**Worst-Case Deterministic Solution**:

- Need to query $n+1$ distinct points to determine if p ≡ 0
- This is because a degree n polynomial could have n roots
- If all $n+1$ queries return $0$, the polynomial must be identically zero

#### How can you recover the coefficients of n$p$ in this model?

- Query $p(s)$ at $s = 0, 1, 2, \dots n$
- Use these evaluations to construct the coefficients via **interpolation**, such as using the **Lagrange interpolation formula**.
- Can use $n+1$ queries to recover all coefficients
- Use linear system of equations from evaluations
- Each query gives an equation: $a_0 + a_1x + a_2x^2 + ... + a_nx^n = p(x)$
- Need $n+1$ equations to solve for n+1 coefficients

### How does randomness help in the polynomial identity testing problem? In particular, which success probability can you achieve using randomness?

- **Schwartz-Zippel Lemma**:
  - Choose evaluation point s randomly from a large enough field
  - If p ≢ 0, probability that p(s) = 0 is ≤ d/|F| where:
    - d is the polynomial degree
    - |F| is the field size
- **Success Probability**:
  - Can achieve error probability ≤ 1/2 with just one random query
  - Can reduce error to 2⁻ᵏ by using k independent random queries
  - This is exponentially better than deterministic approach

## Freivalds’ algorithm

### Describe Freivalds’ algorithm. Make sure to include the following:

#### What is the purpose of Freivalds’ algorithm?

To identify whether two matrices,
Given $A,B,C$ is $A\cdot B=C$
Reformulation: Is AB-C’ the all-zero matrix?
Does NOT compute the product AB, only verifies if a given C equals AB

#### Why is it faster than computing matrix products?

When doing matrix products it takes $n^3$ or theoritacally $n^{2.373}$
Requires computing all n² entries
**Freivalds' Algorithm**:

- Runs in O(n²) time
- Much faster than actually computing the product
- Trades perfect accuracy for speed
- Only needs to perform matrix-vector multiplications

![](pics/svcd.png)

#### Describe the random choices made by the algorithm.

#### Depending on the random choices, when does the algorithm succeed and when does it fail?

![](pics/vds.png)

#### What is the failure probability of the algorithm? Use probability theory to give an argument for your answer

![](pics/cds.png)
![](pics/scds.png)

## Karger’s algorithm:

### What is a global min-cut in a graph?

Given a connected undirected graph, a minimum cut or mincut is a smallest subset of edges that disconnects the graph in two connected components
![](pics/vdfsfvf.png|500)

### Describe Karger’s algorithm to find a global min-cut in a graph.

**Edge contraction**
Given a multigraph (a graph that may have multiple edges between any two vertices), an edge contraction of the edge $e=(u,v)$ collapses u and v into one new vertex $w$, removes all edges between $u$ and $v$, but retain all other edges.

![](pics/fewf.png|500)
**Karger’s original algorithm**

- Repeat n-2 times:
  - Uniformly and independently sample an edge in the (multi)graph and contract it.
- In the end there are only two vertices left.
  Output the edges between them as the min-cut.
  _Key property: we will never make a graph cut smaller. Some cuts vanish, but any cut in a resulting graph is also a cut in the original graph._

![](pics/vdsvs.png|400)
![](pics/svfsvfs.png|400)

### What is the failure probability of Karger’s algorithm? Sketch an analysis using probability theory and highlight where exactly properties of an assumed min-cut are used in the analysis.

Let $G=(V,E)$ let $n=|V|$
Pick some mincut C from G with Size K
($i \geq 0$)
$A_{i}=$ The event that one of the mincut edges in C gets contracted during step i
$G$ has $n$ vertices at step $0$.
We end when we have $2$ vertices left.
Every contraction removes one vertex from $G$.
Contractions $= n-2$

$P(A_{i})=\frac{k}{|E_i|}$
Because we know that k is the smallest amount of edges to anyone vertex for G we have that
$|E|\geq \frac{n \cdot k}{2}$
We can therefore say
$$P(A_{i})=\frac{k}{\frac{n_i \cdot k}{2}}=\frac{2}{n_i}$$
$P(A_i)$ being the chance of messing up
$P(\neg A_i)$ being the chance of NOT messing up
$$P\neg (A_{i})=(1-P(A_{i}))=(1-\frac{2}{n_i})$$

The chance of going all n-2 contractions without contracting an edge in C
$$\prod_{i=0}^{n-3}P(\neg A_{i})=(1-\frac{2}{n_i})$$

but what is $n_i$![](pics/vfsvfvfvs.png|300)
![](pics/vsfvfvfs.png)
$$\frac{(n-2)!\cdot 2}{n!}$$

![](pics/bfgdbgbg.png)

On a graph with n vertices a single run of kargers algorithm will give the actual min-cut with $\binom{n}{2}^{-1}$

##### Multiple runs of kargers algorithm

$P_{s}\geq \frac{1}{\binom{n}{2}}$
$P_{f}\leq 1-\frac{1}{\binom{n}{2}}$
$P(\text{fail})$ for $k$ runs = ${(P_{F})^k}\leq ({1-\frac{1}{\binom{n}{2}}})^k$
==Math rules==
$1-x \leq e^{-x}$
$\binom{n}{2}=\frac{n(n-1)}{2}\leq n^{2}$
**Proof**

$$
\begin{align}
P(\text{fail})
&&\leq ({1-\frac{1}{\binom{n}{2}}})^{k} \newline
&&\leq ({1-\frac{1}{n^{2}}})^{k}\\
&&= ({1-\frac{1}{n^{2}}})^{k} \leq (e^{\frac{1}{n^{2}}})^{k}
\end{align}
$$

If we set $k=n^2$
$P(\text{fail})\leq (e^{\frac{1}{n^{2}}})^{n^2}=e^{\frac{n^{2}}{n^{2}}}=e^{-1}=\frac{1}{e}$
![](pics/bglgl.png)

### Why does the success probability analysis of Karger’s algorithm imply that any graph has at most $\binom{n}{2}$ global min-cuts?

- **Key Insight**:
  - Algorithm succeeds with probability $\binom{n}{2}^{-1}$
  - Each run can find only one specific min-cut
  - If there were more than $\binom{n}{2}$ min-cuts:
    - Sum of probabilities would exceed 1
    - Contradiction!
- **Formal Argument**:
  - Let $m$ be number of distinct min-cuts
  - Each has $\binom{n}{2}^{-1}$ chance of being found
  - Total probability $≤ 1$
  - Therefore: $m ≤ \binom{n}{2}$

## The Monte Carlo method:

### Sketch how you can determine the number $π$ by throwing darts.

![](pics/vfdvbfsb.png)
This is very close to the example from the lecture. 
Essentially, imagine circular dart board with it's center being denoted 0,0. Then the dart board is a circle with radius 1, so the east most point is 1,0 and the north most point is 0,1. 
Imagine a square whose opposite corners are −1,1 and 1,−1. 
The area of the square is 4 and the area of the circle is $π$. 
If we throw darts at the square then the probability of hitting the circle is $π/4$, since that is the ratio of the areas. Then if we throw $n$ darts and m of them hit the circle then $\frac{m}{n} ≈ \frac{π}{4}$, ergo $π≈4 \frac{m}{n}$.
### What does it mean for a randomised algorithm to $(ε,δ)$-approximate a value?
An algorithm is said to approximate the answer if it produces an estimate that is within a factor of $(1+−ϵ)$ of the true answer with probability at least $1−δ$. This means that the algorithm is allowed to be wrong with probability $δ$ and the answer is allowed to be off by a factor of $ϵ$.
### How many samples are sufficient to $(ε,δ)$-approximate the mean $μ$ of an indicator random variable $X$? What is the name of the bound used to prove this? (You don’t need to prove this bound, but have a rough idea how the proof works.)

Chern off bound
Chern off bound
This is the Chernoff bound. The Chernoff bound bounds the sum of independent random variables by providing an upper limit on the probability that the sum deviates from its expected value by more than a certain amount.

When dealing with indicator functions, where $X_i$ is $1$ if an event occurs and $0$ otherwise, then let $S$ be the sum $S=X_1+⋯+X_n$ after $n$ samples and $μ=\frac{S}{n}$ be the mean. This must be within $\epsilon$ of the true mean $μ$ with probability at least $1−δ$.
![](pics/new1.png)
### Consider the following algorithm: To determine the number of satisfying assignments for a Boolean formula $F$ with n variables, randomly sample some number T of assignments. Among those sampled assignments, let $S$ be the number of assignments that satisfy $F$. Then output $S/T * 2^n$.

#### Is the expected output of this algorithm correct?
Yes. $S/T$ represents the fraction of correct assignments in the samples, while 2n is number of assignments in a single correct assignment, as it is the number of possible assignments for n variables. Therefore $S/T∗2^n$ is the expected number of correct assignments.
#### What other problem is there?
If the number of satisfying assigments is very small then the algorithm may not find them unless $T$ is very large, which would make it very slow. Formally if the number of assignments is small compared to $2^n$ then the probability of finding it is very small. This will be solved by the next algorithm.

### Describe the randomized approximation algorithm for counting satisfying assignments to DNFs discussed in class.
If we repeatedly guess an assignment from the $2^n$ possible ones, and see how often it satisfies the formula, we will be able to estimate the number of satisfying assignments. 

Note however, that if there are not that many of them, we might need many samples before we encounter just the first one!

The algorithm works by creating a very small sample space. Imagine a DNF formula, fx: $$ (x_1 \wedge \overline{x_2}\wedge x_3) \vee (x_2\wedge x_4) \vee (\overline{x_1}\wedge x_3\wedge x_4) $$
The algorithm then for each clause $C_i$ in the DNF formula defines the set of assignments that would satisfy it as $SC_i$, the size of this set is $2^{n−l_{i}}$ where $l_{i}$ is the number of literals in the clause

![](pics/clauses_in_bubbles.png)


#### What exactly is the set it samples from?
This can be an absolutely huge set. $t$ is the number of clauses in the DNF formula.

#### Which condition does it check on such a sample?
Define a sampling space
$$U=\{ (i,a):1\leq i \leq t \text{  and  } a \in SC_i \}$$
and note that every assignment that satisfies the formula is represented in $U$. Some assignments are represented many times.

![](pics/clause_estimation.png)

![](pics/samplingOverADenseSpace.png)

#### How does this algorithm solve the problem encountered by the algorithm in the previous bullet point?
The earlier algorithm had the problem that a satisfying assignment might not be found. The difference here is that the sample space is only satisfying assignments which are then sampled from. ==TODO: snak==

## Primality testing -

![](pics/fbvfdvbf.png)

### What is a strong probable prime?

A strong probable prime (also called a strong pseudoprime) is a number that passes a **strengthened version of the Fermat primality test**. Let's understand what this means step by step.

First, recall _Fermat's Little Theorem_: if $p$ is prime and $a$ is not divisible by $p$, then:
$a^{(p-1)} ≡ 1 (\mod p)$

![](pics/kdskdkda.png)

### What is the repeated squaring algorithm? What is its running time?

The algo makes use of:
$a \cdot b \bmod m = (a \bmod m) \cdot (b \bmod m) \mod m$
and the fact that you can split exponents up, and delete some of them when you take them to base 2
![](pics/csd.png)
The idea is we can turn ab into: $$ a^b = a^{2^0b_0+2^1b_1+\dots+2^kb_k} = a^{2^0b_0}a^{2^1b_1}\dots a^{2^kb_k} $$

Where $b_i$ is the $i$th bit of b. The algorithm only does the multiplying when the corresponding digit of b is 1, which also skips some computations. Each computation is also done modulo n, since $a*b \mod n=(a \mod n)(b \mod n)\mod n$. The full algorithm goes as follows:

1. Set $c=1$ and $a_{cur}=a$
2. For $i=0,1,…,k,$ where $k$ is the number of bits in $b$:
    1. If $b_i=1$ then set $c=c*a_{cur} \mod n$
    2. Set $a_{cur}=a_{cur}^{2} \mod n$
3. Return $c$

The running time of the algorithm is $O(\log ⁡b)$, since the number of bits in $b$ is $\log ⁡b$. For each iteration there is at most one multiplication and one squaring operation.
### Describe one algorithm that efficiently checks whether an integer is a prime or not w.h.p.(with high probability)
The Miller-Rabin primality test is a probabilistic algorithm that determines whether a given number is prime or not. It is based on the strong probable prime definition. The algorithm works by:
==TODO ask chat to explain==
![](pics/defw.png)
The algorithm is correct with probability at least $3/4$, and can be made arbitrarily close to $1$ by repeating the process $k$ times. The running time of the algorithm is $O(k \log 3⁡ n)$ for $k$ iterations. This is pretty good as the algorithm usually deals with very large numbers.
## Algebraic algorithms:

### Roughly, what does the DeMillo-Lipton-Schwartz-Zippel lemma say

is a tool commonly used in probabilistic [polynomial identity testing](https://en.wikipedia.org/wiki/Polynomial_identity_testing "Polynomial identity testing"). Identity testing is the problem of determining whether a given multivariate [polynomial](https://en.wikipedia.org/wiki/Polynomial "Polynomial") is the 0-polynomial, the polynomial that ignores all its variables and always returns zero. The lemma states that evaluating a nonzero polynomial on inputs chosen randomly from a large-enough set is likely to find an input that produces a nonzero output.
![](pics/fgfdgfs.png)

Let's start with a single variable case:

- Say $P(x) = ax + b$ is a degree 1 polynomial ($d=1$)
- If $P$ is not identically zero, it has at most 1 root
- If we pick a random value from F, chance of hitting that root is $\frac{1}{|F|}$
- This matches lemma: $\frac{d}{|F|} = \frac{1}{|F|}$

- Think of it as "hitting a target":
  - Polynomial defines a "surface" of zeros
  - Random point has small chance of landing on this surface
  - Larger field = more space = smaller chance of hitting
  - Higher degree = bigger surface = higher chance of hitting
- Why $\frac{d}{|F|}$ bound?
  - Each variable introduces at most degree d constraints
  - Field size $|F|$ represents total possible values
  - Ratio $\frac{d}{|F|}$ represents this constraint/possibility balance

###### Requirements for Field Choice (Claude)

1. **Size Requirement**:
   - Need |F| > d for meaningful probability bound
   - Larger field = better probability bounds (d/|F| gets smaller)
   - Must accommodate coefficient values from original polynomial
2. **Common Field Choices**: a) **Finite Field GF(p)**
   - Where p is prime
   - Elements: {0, 1, ..., p-1}
   - Choose p > d for desired bound
   - Operations are mod p
   - Good for computer implementations

### What is the difference between the two mathematical concepts ring and field?

A field is a set F and two operations addition + and multiplication \* such that

- **Associativity**: $(a+b)+c=a+(b+c)$ and $(a*b)*c=a*(b*c)$.
- **Commutativity**: $a+b=b+a$ and $a*b=b*a$.
- **Identities**: Exist element 0 and 1 such that $a+0=a$ and $a*1=a$.
- **Inverses**: For every element a, there exists an additive inverse $–a$ such that $a+(-a)=0$, and if $a≠0$, there is a multiplicative inverse $a-1$ such that $a*a-1=1$.
- **Distributivity**: $a*(b+c)=(a*b)+(a*c)$

If everything above is fulfilled except the criteria that all non-zero elements have a multiplicative inverse, we instead get a (commutative) ring.

![](pics/brfdgfdg.png|300)

### Name one combinatorial problem matrix determinants can be used to solve and describe roughly how it works.

**Perfect Matching in Bipartite Graphs**
![](pics/kdkdk.png)
**the determinant**
![](pics/dkdkdkd.png)
if the det is not zero

![](pics/dkdkdkdksa.png)
det(A) ≠ 0 iff graph has perfect matching,
however The issue is that a regular biadjacency matrix A (with just 1s and 0s) won't work because:

1. The determinant could be zero even when a perfect matching exists
2. Several different perfect matchings could cancel each other out in the determinant

```
Consider this bipartite graph with vertices {1,2} and {3,4}:
1 -- 3
1 -- 4
2 -- 3
2 -- 4
Its biadjacency matrix would be:
[1 1]
[1 1] The determinant is 0, but the graph clearly has perfect matchings!
```

![](pics/ididid.png)
**Determinant and perfect matchings**

- The determinant of the symbolic matrix is via Leibniz’s formula a sum of signed terms, one for each perfect matching in the graph, given as a product of the variables of the edges in the matching.
- The determinant is hence a non-zero multivariate and multilinear polynomial when there are perfect matchings in the graph.

### How computationally hard is it to compute an nxn symbolic matrix determinant with polynomials in several variables as entries with total degree bounded by $O(n)$? How computationally hard is it to compute an nxn numeric matrix determinant with elements from a finite field as entries?

- Computing the determinant symbolically may require exponential time simply because there may be that many monomials.
- Computing the determinant numerically after we replace each variable with a scalar from some field is a polynomial time task.

##### Symbolic matrix determinant

**Input:**

- n×n matrix
- Entries are polynomials in multiple variables
- Total degree of each polynomial is O(n)

**Complexity Analysis:**

- Output size can be exponential
  - Each term in determinant comes from n entries
  - Total degree of output polynomial is O(n²)
  - Number of terms can be exponential in n

##### Numeric Matrix Determinant (Finite Field)

**Input:**

- n×n matrix
- Entries are elements from finite field F
- Each entry has fixed size

**Complexity:**

- O(n³) field operations
- Each field operation takes constant time
- Total time complexity: O(n³)
- Space complexity: O(n²)

### Describe one way of computing a numeric determinant.

Gaussian elimination
![](pics/disas.png)
Running time is O(n³) using field operations.

## Markov chains:

### What is a Markov chain?

A Markov chain is a mathematical model that describes a sequence of events where the probability of each event depends only on the state of the previous event.
Markov chains are memoryless

**Formally, a Markov chain consists of:**

1. A set of states S
2. Transition probabilities $P(i,j)$ representing the probability of moving from state $i$ to state $j$
3. The Markov property: $P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ..., X_0 = i_0) = P(X_{n+1} = j | X_n = i)$

### What is a stationary solution to a Markov chain?

A stationary solution (or stationary distribution) $π$ is a probability distribution over the states that remains unchanged when we apply the transition matrix. It's like finding a perfect balance where the system has settled into a stable pattern.

Mathematically, $π$ is a vector that satisfies:

1. $π = πP$ (where P is the transition matrix)
2. $Σπi = 1$ (probabilities sum to 1)
3. $πi ≥ 0$ for all $i$ (all probabilities are non-negative)

### What is the cover time of a random walk on a graph?

The cover time of a graph is the maximum over all start vertices v in V of the expected time to visit all the vertices in the graph by a random walk starting from v.

> [!Lemma]
> The cover time of a graph **G=(V,E)** is upper bounded by **4|V||E|**

### Show a tight asymptotic upper bound on the cover time of a random walk on an undirected non-bipartite connected graph.

![](pics/bgbdg.png)

### Show an example of a strongly connected directed graph in which the cover time is exponential.

Here's a striking example of how directed graphs can have exponential cover time:

Consider a directed graph with n vertices arranged in a line:
1 → 2 → 3 → ... → n With additional edges:

- From each vertex i > 1, there's an edge back to vertex 1 with probability 1/2
- The forward edge has probability 1/2

In this graph, reaching vertex n requires taking all forward edges in sequence, which happens with probability $(1/2)^{(n-1)}$. ie the probability of succes with in one go
The expected time to see this sequence is exponential: $2^{(n-1)}$.  
==TODO math ?==

### Describe how the algorithm for 2SAT can be analyzed as a random walk on a graph. What is the graph and what is its cover time?

==TODO graph descripton==

**The problem:**

The 2SAT problem is a boolean formula in conjunctive normal from on n variables with 2 literals in each clause, fx: $$ (x_1 \vee \overline{x_3}) \wedge (\overline{x_1} \vee x_2) \wedge (\overline{x_2} \vee x_4)\wedge (\overline{x_3} \vee \overline{x_4}) $$

The problem is to find an assignment to the variables such that the formula is satisfied. The example has satisfying assignment `
```x1=true,x2=true,x3=false,x4=false.```



Assume a 2SAT formula with n variables has a satisfying assignment and that the 2SAT random walk algorithm is allowed to run until it finds a satisfying assignment. Then the expected number of steps until the algorithm finds a satisfying assignment is at most $n^2$.

Hence, if we abort after $2n^2$ steps, we see from Markov’s inequality that the probability that we don’t find an assignment when there is one, is at most ½.

**Markovs inequality**
![](pics/fewfwef.png)![](pics/wefewf.png)

![](pics/werw.png)
![](pics/vfvfs.png)
![](pics/vfvdf.png)

![](pics/whiteboard_proof_chern.png)