## Divide & Conquer and the Master theorem

### Give the statement of the Master theorem for recurrence relations of the form $T(𝑛) ≤ 𝑎𝑇(𝑛/𝑏) + 𝑂(𝑛^𝑐)$ Explain which cases can occur depending on a,b,c

![](pics/IMG_2700.jpeg)

![](pics/IMG_2699.jpeg|700)

### Sketch a proof for one of the cases.

==TODO:HELP==

## Integer Multiplication

### What is Karatsuba’s algorithm?

Karatsuba's algorithm is a divide-and-conquer method for multiplying two integers more efficiently than the standard "grade-school" approach. $O(n^2)$
![](pics/IMG_2698.jpeg|200)
It reduces the number of multiplications required, which is the most computationally expensive operation in integer multiplication.

The trick is to get to down to **three** recursive calls, as if we do four, it will lead to $n^2$
![](pics/kf.png)

![](pics/pd.png)
![](pics/lsl.png)

![](pics/IMG_2701.jpeg)

### What is its running time?

From master thm
![](pics/IMG_2700 1.jpeg|500)
3 way branching, split factor of 2, because we halve the number of bits each time we branch
![](pics/ps.png)
![](pics/ls.png)
