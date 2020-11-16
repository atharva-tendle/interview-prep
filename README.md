# interview-prep
Collection of datastructures, algorithms and problems.


## Big-O Notation

 - Gives an **upper bound** of the complexity in the **worst** case. (as **input size** increases how is the performance impacted?)
 - This applies to both ***time*** and ***space*** complexities.

n : size of the input

```
     | O(1)       :- Constant Time
     | O(log(n))  :- Logarithmic Time
 T   | O(n)       :- Linear Time
 I   | O(nlog(n)) :- Linearithmic Time
 M   | O(n^2)     :- Quadratic Time
 E   | O(n^3)     :- Cubic Time
     | O(x^n)     :- Exponential Time (x > 1)
     v O(n!)      :- Factorial Time
```
Properties:
```
O(n + c) = O(n) (c is a constant)
O(cn) = O(n) (c > 0)

Eg: g(n) = 10n^3 + 4n + 2, O(g(n)) = O(n^3)