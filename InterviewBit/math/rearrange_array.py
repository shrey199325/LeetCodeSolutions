"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
"""


class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        # In this ques since the man number would be (len(A)-1) so
        # len(A) can be taken as the number for increment.
        # If the case is not mentioned, use max(A)
        for i in range(0, n):
            A[i] += (A[A[i]] % n) * n
        for i in range(0, n):
            A[i] = A[i] // n
