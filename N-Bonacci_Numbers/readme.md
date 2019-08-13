N-bonacci numbers



The Fibonacci sequence is a set of numbers that starts with a one or a zero, followed by a one, and proceeds based on the rule that each number is equal to the sum of the preceding two numbers: 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...



We can generalize this to an N-bonacci sequence, where the sum of the preceding N  numbers form the next term. 

For example, a 3-bonacci sequence is the following:

0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, ...



Write a program which takes two inputs: N and M, and gets the M-th term of any N-bonacci sequence.



For example:

Input: (N, M) = (4, 13)

Output: 0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208



Bonus: Try to solve this both recursively and iteratively.