This program finds in the OEIS, series of numbers produced by the binet formula with a combination of trascendental numbers.
Its not intended to bruteforce the OEIS database but to find new relations in the existing formulas.

With integers a and b in the range of 0,10.
```
0, 1, A047999, Sierpiński's [Sierpinski's] triangle (or gasket): triangle, read by rows, formed by reading Pascal's triangle mod 2.
0, 2, A034008, a(n) = floor(2^|n-1|/2). Or: 1, 0, followed by powers of 2.
0, 3, A140429, a(n) = floor(3^(n-1)).
1, 2, A000225, a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usually reserved for A001348.)
1, 3, A003462, a(n) = (3^n - 1)/2.
1, 4, A002450, a(n) = (4^n - 1)/3.
1, 5, A003463, a(n) = (5^n - 1)/4.
1, 6, A003464, a(n) = (6^n - 1)/5.
1, 7, A023000, a(n) = (7^n - 1)/6.
1, 8, A023001, a(n) = (8^n - 1)/7.
1, 9, A002452, a(n) = (9^n - 1)/8.
2, 3, A001047, a(n) = 3^n - 2^n.
2, 4, A006516, a(n) = 2^(n-1)*(2^n - 1), n >= 0.
3, 4, A005061, a(n) = 4^n - 3^n.
3, 5, A005059, a(n) = (5^n - 3^n)/2.
4, 5, A005060, a(n) = 5^n - 4^n.
4, 6, A081199, 5th binomial transform of (0,1,0,1,...), A000035.
4, 8, A016152, a(n) = 4^(n-1)*(2^n-1).
4, 9, A016153, (9^n-4^n)/5.
5, 6, A005062, a(n) = 6^n - 5^n.
5, 7, A081200, 6th binomial transform of (0,1,0,1,0,1,....), A000035.
6, 7, A016169, a(n) = 7^n - 6^n.
6, 8, A081201, 7th binomial transform of (0,1,0,1,0,1,....), A000035.
7, 8, A016177, a(n) = 8^n - 7^n.
7, 9, A081202, 8th binomial transform of (0,1,0,1,0,1,....), A000035.
8, 9, A016185, a(n) = 9^n - 8^n.
```

With combinations of trascendental numbers:
```
0, 15, 2, A002264, Nonnegative integers repeated 3 times.
0, 15, 4, A000523, a(n) = floor(log_2(n)).
0, 21, 2, A332062, Number of iterations of z -> z^2 + 1/4 + 1/2^n until z > 2, starting with z = 0.
1, 15, 2, A072493, a(1) = 1 and a(n) = ceiling((Sum_{k=1..n-1} a(k))/3) for n >= 2.
1, 15, 4, A000931, Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = 0.
1, 20, 4, A209888, Number of binary words of length n containing no subword 01101.
5, 15, 4, A073031, Number of ways of making change for n cents using coins of sizes 1, 2, 5, 10 cents, when order matters.
6, 15, 2, A015753, Number of partitions of n into distinct parts, none being 6.
6, 15, 4, A003114, Number of partitions of n into parts 5k+1 or 5k+4.
6, 21, 4, A048818, Denominators of convergents to A058914.
7, 15, 2, A000196, Integer part of square root of n. Or, number of positive squares <= n. Or, n appears 2n+1 times.
7, 15, 4, A132211, Coefficients of a Ramanujan q-series.
7, 21, 2, A046682, Number of cycle types of conjugacy classes of all even permutations of n elements.
7, 21, 4, A102543, Antidiagonal sums of the antidiagonals of Losanitsch's triangle.
8, 15, 2, A238861, Compositions with superdiagonal growth: number of compositions (p0, p1, p2, ...) of n with pi - p0 >= i.
8, 15, 4, A024186, Expansion of Molien series for 8-dimensional real Clifford group 2^{1+6}.Alt_8.2 of genus 3 and order 5160960.
8, 21, 2, A227376, G.f.: 1/(1 - x - x^2 - x^3 + x^5 + x^6 + x^7).
9, 15, 2, A052816, G.f.: (1+x)*Product_{m>0} (1 + x^m).
9, 15, 4, A000931, Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = 0.
9, 21, 2, A289168, Length of n-th iterate of the mapping 00->0010, 01->100, 10->001 in A289165.
10, 15, 2, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
10, 15, 4, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
10, 20, 2, A038348, Expansion of (1/(1-x^2))*Product_{m>=0} 1/(1-x^(2m+1)).
10, 20, 4, A238861, Compositions with superdiagonal growth: number of compositions (p0, p1, p2, ...) of n with pi - p0 >= i.
10, 21, 2, A000607, Number of partitions of n into prime parts.
10, 21, 4, A053251, Coefficients of the '3rd order' mock theta function psi(q)
12, 15, 1, A186085, Number of 1-dimensional sand piles with n grains.
12, 15, 2, A123706, Matrix inverse of triangle A010766, where A010766(n,k) = [n/k], for n>=k>=1.
12, 15, 4, A228591, Determinant of the n X n (0,1)-matrix with (i,j)-entry equal to 1 if and only if i + j is 2 or an odd composite number.
12, 20, 2, A000196, Integer part of square root of n. Or, number of positive squares <= n. Or, n appears 2n+1 times.
12, 20, 4, A306216, Successive concatenation of the current sequence with the first differences of the sequence, a(1) = a(2) = 1.
12, 21, 0, A004698, a(n) = floor(Fibonacci(n)/5).
12, 21, 1, A001595, a(n) = a(n-1) + a(n-2) + 1, with a(0) = a(1) = 1.
12, 21, 2, A118914, Table of the prime signatures (sorted lists of exponents of distinct prime factors) of the positive integers.
12, 21, 4, A055642, Number of digits in decimal expansion of n.
12, 22, 4, A023434, Dying rabbits: a(n) = a(n-1) + a(n-2) - a(n-4).
13, 14, 3, A057084, Scaled Chebyshev U-polynomials evaluated at sqrt(2).
13, 15, 2, A087897, Number of partitions of n into odd parts greater than 1.
13, 15, 3, A057084, Scaled Chebyshev U-polynomials evaluated at sqrt(2).
13, 15, 4, A002264, Nonnegative integers repeated 3 times.
13, 21, 4, A206742, G.f.: 1/(1 - x/(1 - x^3/(1 - x^4/(1 - x^7/(1 - x^11/(1 - x^18/(1 -...- x^Lucas(n)/(1 -...)))))))), a continued fraction.
14, 15, 0, A000129, Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2).
14, 15, 1, A080617, Consider 3 X 3 X 3 Rubik cube, but only allow the moves M_R, D; sequence gives number of positions that are exactly n moves from the start.
14, 15, 2, A306216, Successive concatenation of the current sequence with the first differences of the sequence, a(1) = a(2) = 1.
14, 15, 3, A002315, NSW numbers: a(n) = 6*a(n-1) - a(n-2); also a(n)^2 - 2*b(n)^2 = -1 with b(n)=A001653(n+1).
14, 15, 4, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
14, 20, 4, A117791, Expansion of 1/(1 - x - x^2 + x^4 - x^6).
14, 21, 2, A060967, Number of squared primes <= 2^n.
14, 21, 4, A020999, Conjectured number of irreducible multiple zeta values of depth n and weight 3n (confirmed up to n=7).
15, 16, 3, A008813, Expansion of (1+x^6)/((1-x)^2*(1-x^6)).
15, 17, 1, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
15, 17, 3, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
15, 18, 0, A113788, Number of irreducible multiple zeta values at weight n.
15, 18, 1, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
15, 18, 2, A003114, Number of partitions of n into parts 5k+1 or 5k+4.
15, 18, 3, A047999, Sierpiński's [Sierpinski's] triangle (or gasket): triangle, read by rows, formed by reading Pascal's triangle mod 2.
15, 19, 0, A124502, a(1)=a(2)=1; thereafter, a(n+1) = a(n) + a(n-1) + 1 if n is a multiple of 5, otherwise a(n+1) = a(n) + a(n-1).
15, 19, 1, A123706, Matrix inverse of triangle A010766, where A010766(n,k) = [n/k], for n>=k>=1.
15, 19, 2, A181600, Expansion of 1/(1 - x - x^2 + x^8 - x^10).
15, 19, 3, A228591, Determinant of the n X n (0,1)-matrix with (i,j)-entry equal to 1 if and only if i + j is 2 or an odd composite number.
15, 20, 0, A123706, Matrix inverse of triangle A010766, where A010766(n,k) = [n/k], for n>=k>=1.
15, 20, 1, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
15, 20, 2, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
15, 20, 3, A047999, Sierpiński's [Sierpinski's] triangle (or gasket): triangle, read by rows, formed by reading Pascal's triangle mod 2.
15, 20, 4, A117791, Expansion of 1/(1 - x - x^2 + x^4 - x^6).
15, 20, 5, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
15, 21, 0, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
15, 21, 1, A121373, Expansion of f(x) = f(x, -x^2) in powers of x where f(, ) is Ramanujan's general theta function.
15, 21, 2, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
15, 21, 3, A123706, Matrix inverse of triangle A010766, where A010766(n,k) = [n/k], for n>=k>=1.
15, 21, 4, A020999, Conjectured number of irreducible multiple zeta values of depth n and weight 3n (confirmed up to n=7).
15, 21, 5, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
15, 22, 0, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
15, 22, 1, A121373, Expansion of f(x) = f(x, -x^2) in powers of x where f(, ) is Ramanujan's general theta function.
15, 22, 2, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
15, 22, 3, A228591, Determinant of the n X n (0,1)-matrix with (i,j)-entry equal to 1 if and only if i + j is 2 or an odd composite number.
15, 22, 5, A000009, Expansion of Product_{m >= 1} (1 + x^m); number of partitions of n into distinct parts; number of partitions of n into odd parts.
15, 23, 1, A123706, Matrix inverse of triangle A010766, where A010766(n,k) = [n/k], for n>=k>=1.
15, 23, 2, A098855, Numbers n such that 4^n + 2^n - 1 is prime.
15, 23, 3, A228591, Determinant of the n X n (0,1)-matrix with (i,j)-entry equal to 1 if and only if i + j is 2 or an odd composite number.
16, 18, 0, A063727, a(n) = 2*a(n-1) + 4*a(n-2), a(0)=1, a(1)=2.
17, 19, 3, A030191, Scaled Chebyshev U-polynomial evaluated at sqrt(5)/2.
17, 20, 3, A030191, Scaled Chebyshev U-polynomial evaluated at sqrt(5)/2.
17, 21, 2, A058360, Number of partitions of n whose reciprocal sum is an integer.
17, 21, 4, A000607, Number of partitions of n into prime parts.
18, 20, 0, A060863, Positive numbers n which are the average of a run of consecutive primes.
18, 20, 1, A261736, Expansion of Product_{k>=1} (1 + x^(6*k))/(1 + x^k).
18, 20, 2, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
18, 20, 4, A047999, Sierpiński's [Sierpinski's] triangle (or gasket): triangle, read by rows, formed by reading Pascal's triangle mod 2.
18, 21, 0, A104410, Coefficients of the C-Rogers-Selberg identity.
18, 21, 1, A003401, Numbers of edges of regular polygons constructible with ruler (or, more precisely, an unmarked straightedge) and compass.
18, 21, 2, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
18, 21, 4, A229658, 8-section a(8n+k) gives k-th differences of a for k=0..7 with a(n)=0 for n<7 and a(7)=1.
18, 22, 0, A261736, Expansion of Product_{k>=1} (1 + x^(6*k))/(1 + x^k).
18, 22, 4, A003056, n appears n+1 times. Also the array A(n,k) = n+k (n >= 0, k >= 0) read by antidiagonals. Also inverse of triangular numbers.
19, 20, 0, A290689, Number of transitive rooted trees with n nodes.
19, 20, 2, A000196, Integer part of square root of n. Or, number of positive squares <= n. Or, n appears 2n+1 times.
19, 20, 4, A306216, Successive concatenation of the current sequence with the first differences of the sequence, a(1) = a(2) = 1.
19, 21, 0, A293673, a(n) is the integer k that minimizes |k/Fibonacci(n) - 4/5|.
19, 21, 2, A118914, Table of the prime signatures (sorted lists of exponents of distinct prime factors) of the positive integers.
19, 21, 4, A055642, Number of digits in decimal expansion of n.
19, 22, 4, A323360, Least number of consecutive primes beginning with 2, the sum of which (A007504) is >= 2^n.
20, 21, 0, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
20, 21, 1, A228591, Determinant of the n X n (0,1)-matrix with (i,j)-entry equal to 1 if and only if i + j is 2 or an odd composite number.
20, 21, 2, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
20, 21, 3, A036468, Number of ways to represent 2n+1 as a+b with 0 < a < b and a^2 + b^2 prime.
20, 21, 4, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
20, 21, 5, A003056, n appears n+1 times. Also the array A(n,k) = n+k (n >= 0, k >= 0) read by antidiagonals. Also inverse of triangular numbers.
20, 22, 0, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
20, 22, 1, A229658, 8-section a(8n+k) gives k-th differences of a for k=0..7 with a(n)=0 for n<7 and a(7)=1.
20, 22, 2, A010815, From Euler's Pentagonal Theorem: coefficient of q^n in Product_{m>=1} (1 - q^m).
20, 22, 3, A305940, Irregular triangle where T(n,k) is the coefficient of s(y) in p(n), where s is Schur functions, p is power-sum symmetric functions, and y is the integer partition with Heinz number A215366(n,k).
20, 22, 4, A323360, Least number of consecutive primes beginning with 2, the sum of which (A007504) is >= 2^n.
20, 22, 5, A048597, Very round numbers: reduced residue system consists of only primes and 1.
20, 23, 0, A051449, Fibered rational knots with n crossings.
20, 23, 1, A280560, a(n) = (-1)^n * 2 if n!=0, with a(0) = 1.
20, 23, 2, A127968, a(n) = F(n+1) + (1-(-1)^n)/2, where F() = Fibonacci numbers A000045.
20, 23, 3, A070750, 0 if n-th prime is even, 1 if n-th prime is == 1 mod 4, and -1 if n-th prime is == 3 mod 4.
21, 22, 0, A055642, Number of digits in decimal expansion of n.
21, 22, 1, A047999, Sierpiński's [Sierpinski's] triangle (or gasket): triangle, read by rows, formed by reading Pascal's triangle mod 2.
21, 22, 2, A055642, Number of digits in decimal expansion of n.
21, 22, 3, A079944, A run of 2^n 0's followed by a run of 2^n 1's, for n=0, 1, 2, ...
21, 22, 4, A266331, a(n) is the integer part of r^n  where  r^2 = Sum_{n>=1} 1/a(n).
21, 22, 5, A006207, Generalized Fibonacci numbers A_{n,2}.
21, 23, 1, A055642, Number of digits in decimal expansion of n.
21, 23, 3, A047999, Sierpiński's [Sierpinski's] triangle (or gasket): triangle, read by rows, formed by reading Pascal's triangle mod 2.
22, 23, 3, A002569, Max_{k=0..n} { Number of partitions of n into exactly k parts }.

```

